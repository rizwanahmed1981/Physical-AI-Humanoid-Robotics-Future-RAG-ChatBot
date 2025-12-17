---
title: Chapter 2 Section 3 Quiz - Understanding Nodes, Topics, Services, and Actions
sidebar_label: Chapter 2 Section 3 Quiz
---

import MCQQuiz from '@site/src/components/MCQQuiz';

# Chapter 2 Section 3 Quiz: Understanding Nodes, Topics, Services, and Actions

<MCQQuiz
  title="Understanding Nodes, Topics, Services, and Actions"
  questions={[
    {
      question: "What are nodes in ROS 2?",
      answers: [
        { text: "Physical hardware components", correct: false },
        { text: "The basic computational units that perform processing", correct: true },
        { text: "Communication channels", correct: false },
        { text: "Special types of sensors", correct: false }
      ],
      explanation: "Nodes are the fundamental building blocks of a ROS 2 system, each being a process that performs computation."
    },
    {
      question: "What type of communication pattern do topics use?",
      answers: [
        { text: "Request-response", correct: false },
        { text: "Publish-subscribe", correct: true },
        { text: "Peer-to-peer", correct: false },
        { text: "Broadcast-only", correct: false }
      ],
      explanation: "Topics use the publish-subscribe pattern where publishers send messages to topics and subscribers receive them."
    },
    {
      question: "When should you use services in ROS 2?",
      answers: [
        { text: "For continuous data streams", correct: false },
        { text: "For tasks with clear beginning and end that need immediate response", correct: true },
        { text: "For long-running tasks with feedback", correct: false },
        { text: "For hardware connections only", correct: false }
      ],
      explanation: "Services are appropriate for tasks that have a clear beginning and end, such as saving a map or calculating inverse kinematics."
    },
    {
      question: "What makes actions different from services?",
      answers: [
        { text: "Actions are faster than services", correct: false },
        { text: "Actions provide continuous feedback and can be canceled", correct: true },
        { text: "Actions use less memory", correct: false },
        { text: "Actions are only for hardware", correct: false }
      ],
      explanation: "Actions are designed for long-running tasks that provide continuous feedback and can be canceled, unlike services which are synchronous and immediate."
    },
    {
      question: "Which communication type is best for sensor data like camera images?",
      answers: [
        { text: "Services", correct: false },
        { text: "Actions", correct: false },
        { text: "Topics", correct: true },
        { text: "Direct connections", correct: false }
      ],
      explanation: "Topics are ideal for continuous data streams like sensor data, where multiple nodes might need to receive the same information simultaneously."
    }
  ]}
/>