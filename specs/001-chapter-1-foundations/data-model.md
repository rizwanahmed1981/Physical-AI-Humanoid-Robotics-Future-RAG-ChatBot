# Data Model: Foundations of Physical AI

## Chapter Entity

**Chapter**: Represents a learning unit with specific content and learning objectives

- **chapter_id**: Unique identifier for the chapter (string)
- **title**: Title of the chapter (string)
- **description**: Brief overview of chapter content (string)
- **sections**: Array of section objects (array)
- **learning_outcomes**: Array of learning objectives (array)
- **quiz_requirements**: Object specifying quiz structure (object)

## Section Entity

**Section**: Represents a subdivision within a chapter

- **section_id**: Unique identifier for the section (string)
- **title**: Title of the section (string)
- **content**: Main content of the section (string)
- **subsection_count**: Number of subsections (integer)
- **formative_quizzes**: Array of formative quiz objects (array)
- **comprehensive_quiz**: Comprehensive quiz object (object)

## Quiz Entity

**Quiz**: Assessment tool with formative and comprehensive questions

- **quiz_id**: Unique identifier for the quiz (string)
- **type**: "formative" or "comprehensive" (string)
- **questions**: Array of question objects (array)
- **reveal_button_label**: Label for answer reveal button (string)

## Question Entity

**Question**: Individual quiz question with multiple choices

- **question_id**: Unique identifier for the question (string)
- **text**: The question content (string)
- **choices**: Array of answer choice objects (array)
- **correct_answer_id**: Identifier for the correct choice (string)
- **explanation**: Brief explanation of why the answer is correct (string)

## Choice Entity

**Choice**: Individual answer choice for a question

- **choice_id**: Unique identifier for the choice (string)
- **text**: The choice text (string)
- **is_correct**: Boolean indicating if this is the correct answer (boolean)