---
title: Chapter 2 Section 1 Quiz - Why ROS 2 Exists
sidebar_label: Chapter 2 Section 1 Quiz
---

import MCQQuiz from '@site/src/components/MCQQuiz';

# Chapter 2 Section 1 Quiz: Why ROS 2 Exists

<MCQQuiz
  title="Why ROS 2 Exists"
  questions={[
    {
      question: "What is the primary purpose of ROS 2?",
      answers: [
        { text: "To serve as a traditional operating system for robots", correct: false },
        { text: "To provide a communication framework for robot software components", correct: true },
        { text: "To replace all other robot software", correct: false },
        { text: "To eliminate the need for programming robots", correct: false }
      ],
      explanation: "ROS 2 provides a communication framework that allows different robot software components to interact with each other without direct coupling."
    },
    {
      question: "What challenge does ROS 2 address in robotics?",
      answers: [
        { text: "The need for faster processors", correct: false },
        { text: "The communication challenge between multiple robot components", correct: true },
        { text: "The need for more sensors", correct: false },
        { text: "The need for better batteries", correct: false }
      ],
      explanation: "ROS 2 addresses the complex communication challenge of coordinating between dozens of sensors, actuators, and processing units in a robot."
    },
    {
      question: "How does ROS 2 enable modularity in robotic systems?",
      answers: [
        { text: "By requiring all components to be written in the same language", correct: false },
        { text: "By providing standardized communication primitives that allow independent development", correct: true },
        { text: "By eliminating the need for communication between components", correct: false },
        { text: "By requiring all components to run on the same computer", correct: false }
      ],
      explanation: "ROS 2 provides standardized communication primitives (topics, services, actions) that allow different components to be developed independently and then integrated."
    },
    {
      question: "What would happen without ROS 2 or similar frameworks in complex robots?",
      answers: [
        { text: "Robots would be more efficient", correct: false },
        { text: "Each component would need to know about every other component, creating complex connections", correct: true },
        { text: "Robots would be cheaper to build", correct: false },
        { text: "Robots would be faster", correct: false }
      ],
      explanation: "Without communication frameworks, each component would need direct knowledge of every other component, leading to an impossibly complex web of connections."
    },
    {
      question: "Which of these is NOT a benefit of ROS 2's approach?",
      answers: [
        { text: "Modularity", correct: false },
        { text: "Reusability", correct: false },
        { text: "Scalability", correct: false },
        { text: "Elimination of all communication", correct: true }
      ],
      explanation: "ROS 2 facilitates communication between components, it doesn't eliminate it. The benefits include modularity, reusability, and scalability."
    }
  ]}
/>