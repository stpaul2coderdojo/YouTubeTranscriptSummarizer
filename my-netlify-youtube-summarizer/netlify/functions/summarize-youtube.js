const { YouTubeTranscriptApi } = require('youtube-transcript-api');
const { pipeline } = require('transformers');
const rx = require('rxjs');
const { from } = rx;
const { map, reduce } = require('rxjs/operators');

exports.handler = async function(event, context) {
    const vID = event.queryStringParameters.vID;

    if (!vID) {
        return {
            statusCode: 400,
            body: JSON.stringify({ error: 'Video ID is required' }),
        };
    }

    try {
        const transcriptList = await YouTubeTranscriptApi.listTranscripts(vID);
        const transcripts = await transcriptList[0].fetch();
        
        const source = from(transcripts);
        const textObservable = source.pipe(
            map(c => c.text),
            reduce((acc, text) => acc + text + ' ', '')
        );

        let transcriptText = await new Promise((resolve, reject) => {
            textObservable.subscribe({
                next: resolve,
                error: reject,
            });
        });

        const summarizer = pipeline('summarization');
        const summary = await summarizer(transcriptText, { max_length: 512 });

        return {
            statusCode: 200,
            body: JSON.stringify(summary),
        };
    } catch (error) {
        return {
            statusCode: 500,
            body: JSON.stringify({ error: error.message }),
        };
    }
};
