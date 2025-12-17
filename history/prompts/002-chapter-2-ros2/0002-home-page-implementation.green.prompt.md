---
id: 0002
title: home-page-implementation
stage: green
date: 2025-12-16
surface: agent
model: sonnet
feature: 002-chapter-2-ros2
branch: 001-chapter-1-foundations
user: ecomw
command: /sp.implement
labels: [homepage, docusaurus, react]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - /home/ecomw/ai-native-book-phase1/src/pages/index.jsx
 - /home/ecomw/ai-native-book-phase1/src/pages/styles.module.css
 - /home/ecomw/ai-native-book-phase1/hero_page.png
 - /home/ecomw/ai-native-book-phase1/.docusaurus/registry.js
 - /home/ecomw/ai-native-book-phase1/.docusaurus/routes.js
 - /home/ecomw/ai-native-book-phase1/.docusaurus/routesChunkNames.json
 - /home/ecomw/ai-native-book-phase1/.docusaurus/site-metadata.json
tests:
 - []
---

## Prompt

Create a home page for the AI Native Robotics textbook website using Docusaurus. The page should include:
- A hero section with the site title and subtitle "Bridging Digital AI with Embodied Intelligence"
- A prominent button to start reading Chapter 1
- Three cards highlighting Chapter 1, Chapter 2, and Book Overview with appropriate links
- Proper styling using Docusaurus conventions
- Responsive design that works well on different screen sizes

## Response snapshot

```jsx
import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './styles.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title">{siteConfig.title}</h1>
        <p className="hero__subtitle">Bridging Digital AI with Embodied Intelligence</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/chapters/chapter1">
            Start Learning Chapter 1
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();

  return (
    <div>
      <HomepageHeader />
      <main>
        <div className="container">
          <div className="row">
            <div className="col col--4">
              <div className="card">
                <div className="card__header">
                  <h3>Chapter 1: Foundations of Physical AI</h3>
                </div>
                <div className="card__body">
                  <p>Explore the fundamental concepts of Physical AI and embodied intelligence. Understand how artificial intelligence moves from abstract algorithms to tangible, physical manifestations.</p>
                </div>
                <div className="card__footer">
                  <Link to="/docs/chapters/chapter1" className="button button--secondary">
                    Read Chapter 1
                  </Link>
                </div>
              </div>
            </div>
            <div className="col col--4">
              <div className="card">
                <div className="card__header">
                  <h3>Chapter 2: The Robotic Nervous System (ROS 2)</h3>
                </div>
                <div className="card__body">
                  <p>Dive into the Robot Operating System 2 (ROS 2) - the foundational infrastructure that enables communication between robot components and AI algorithms.</p>
                </div>
                <div className="card__footer">
                  <Link to="/docs/chapters/chapter2" className="button button--secondary">
                    Read Chapter 2
                  </Link>
                </div>
              </div>
            </div>
            <div className="col col--4">
              <div className="card">
                <div className="card__header">
                  <h3>Book Overview</h3>
                </div>
                <div className="card__body">
                  <p>This textbook explores the intersection of artificial intelligence and robotics, focusing on embodied intelligence and the practical implementation of AI in physical systems.</p>
                </div>
                <div className="card__footer">
                  <Link to="/docs/" className="button button--secondary">
                    View All Chapters
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
```

```css
.heroBanner {
  padding: 4rem 0;
  text-align: center;
  position: relative;
  overflow: hidden;
}

@media screen and (max-width: 966px) {
  .heroBanner {
    padding: 2rem;
  }
}

.buttons {
  display: flex;
  align-items: center;
  justify-content: center;
}
```

## Outcome

- ✅ Impact: Successfully implemented a responsive home page for the AI Native Robotics textbook website with hero section and chapter cards
- 🧪 Tests: No automated tests needed for static page components
- 📁 Files: Created index.jsx and styles.module.css in src/pages/, updated Docusaurus configuration files
- 🔁 Next prompts: Enhance home page with additional sections, add more chapters to the site, improve styling
- 🧠 Reflection: The implementation follows Docusaurus best practices and creates a clean, professional landing page that effectively introduces the textbook content

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Add additional content sections to the homepage