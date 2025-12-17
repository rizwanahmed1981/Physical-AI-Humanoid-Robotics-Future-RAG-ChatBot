# Docusaurus Skill

## Overview
This skill enables creating and managing documentation projects using Docusaurus, a modern static website generator optimized for publishing documentation.

## Purpose
Create, maintain, and deploy documentation sites using Docusaurus framework following Spec-Driven Development principles.

## Commands
- `/sp.docusaurus.init` - Initialize a new Docusaurus project
- `/sp.docusaurus.create-doc` - Create a new documentation page
- `/sp.docusaurus.build` - Build the documentation site
- `/sp.docusaurus.deploy` - Deploy the documentation site

## Implementation Approach
Following Spec-Driven Development principles:
1. Define documentation requirements and scope
2. Create project structure aligned with Docusaurus conventions
3. Implement documentation content with proper metadata
4. Configure build and deployment pipeline
5. Validate documentation quality and accessibility

## Prerequisites
- Node.js >= 16.14
- npm or yarn package manager
- Git for version control

## Best Practices
- Use semantic versioning for documentation
- Implement proper navigation structure
- Follow Docusaurus's recommended folder structure
- Include proper metadata for SEO and discoverability
- Ensure responsive design for all devices

## Usage Examples

### Initialize Docusaurus Project
```
/sp.docusaurus.init --name my-docs --template classic
```

### Create Documentation Page
```
/sp.docusaurus.create-doc --title "Getting Started" --category guides
```

### Build Documentation Site
```
/sp.docusaurus.build
```

### Deploy Documentation Site
```
/sp.docusaurus.deploy --target github-pages
```