

```markdown
# YouTube Summarizer

This project is a web application that allows users to input a YouTube video ID, fetches the transcript of the video, and summarizes it using a Hugging Face summarization model. The app is deployed using Netlify, with serverless functions to handle the backend logic.

## Features

- Fetches YouTube video transcripts.
- Summarizes transcripts using a Hugging Face model.
- Deployed on Netlify with serverless functions.

## Technologies Used

- Netlify for deployment and serverless functions.
- YouTube Transcript API for fetching video transcripts.
- Hugging Face Transformers for summarization.
- RxJS for reactive programming.
- HTML, CSS, and JavaScript for the frontend.

## Project Structure

```
my-netlify-youtube-summarizer/
├── netlify/
│   └── functions/
│       └── summarize-youtube.js
├── public/
│   └── index.html
├── netlify.toml
├── package.json
├── package-lock.json
└── node_modules/
```

## Getting Started

### Prerequisites

- Node.js and npm installed on your machine.
- Netlify CLI installed globally (`npm install -g netlify-cli`).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/stpaul2coderdojo/my-netlify-youtube-summarizer.git
   cd my-netlify-youtube-summarizer
   ```

2. Install the dependencies:
   ```bash
   npm install
   ```

### Configuration

Make sure your `netlify.toml` file is correctly configured:

```toml
[build]
  command = "npm run build"
  publish = "public"

[functions]
  directory = "netlify/functions"
```

### Running Locally

To run the application locally with Netlify Dev:

```bash
netlify dev
```

This command will start a local development server with your functions and frontend.

### Building the Project

To build the project for production:

```bash
npm run build
```

This command will copy the contents of the `public` directory to the `dist` directory.

### Deploying to Netlify

1. Log in to Netlify:
   ```bash
   netlify login
   ```

2. Deploy the site:
   ```bash
   netlify deploy --prod
   ```

## Usage

1. Open the deployed application in your browser.
2. Enter a YouTube video ID into the input field.
3. Click the "Summarize" button.
4. View the summarized transcript in the output area.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Netlify](https://www.netlify.com/)
- [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [RxJS](https://rxjs.dev/)

```

This `README.md` provides an overview of the project, setup instructions, and details on how to run and deploy the application.
 
