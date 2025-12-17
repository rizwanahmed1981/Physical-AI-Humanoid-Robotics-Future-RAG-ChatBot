# Physical-AI-Humanoid-Robotics Textbook

This directory contains the frontend application for the Physical-AI-Humanoid-Robotics textbook, built with Docusaurus.

## Architecture

The frontend is a Docusaurus-based documentation site that presents the textbook content in an interactive format with embedded quizzes and assessments.

## Getting Started

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

4. Build for production:
```bash
npm run build
```

## Directory Structure

```
frontend/
├── docs/                 # Documentation content
├── src/                  # Source code and components
├── static/               # Static assets
├── docusaurus.config.js  # Docusaurus configuration
├── sidebars.js           # Sidebar navigation
├── package.json          # Dependencies and scripts
└── README.md             # This file
```

## Features

- Interactive textbook content with structured sections
- Embedded quizzes for formative assessment
- Comprehensive chapter quizzes
- Responsive design for all devices
- GitHub Pages compatible deployment

## Deployment

The frontend is configured to be deployed to GitHub Pages. The build process creates optimized static assets that can be served directly from a GitHub Pages site.

For deployment, run:
```bash
npm run build
```

Then deploy the contents of the `build/` directory to your GitHub Pages site.