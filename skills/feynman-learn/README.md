[中文说明](README_zh.md)

# feynman-learn

feynman-learn is a Feynman explanation skill. It helps the assistant explain complex knowledge through a beginner-friendly story, then attach the technical points back to that story.

The skill is useful when the user wants to:

- Understand a concept, mechanism, distinction, or process
- Explain a technical topic to a non-expert
- Learn a pipeline or training flow
- Check whether their own explanation is clear
- Build a knowledge map or learning plan when explicitly requested

## Core Idea

The skill should make the user understand, not make the assistant look comprehensive.

A good explanation:

- Starts with one familiar picture from everyday life
- Uses that picture as the backbone of the explanation
- Maps each technical term to a role, action, or result in the story
- Explains processes by saying what existed before and what changed after
- Leaves the user with one sentence they can repeat

## How It Behaves

For a normal concept question, it explains the idea through a familiar story and a small example.

For a process question, it follows the main line of the story and shows how each step changes the situation.

For a knowledge-map or learning-plan question, it gives structure and sequence because the user explicitly asked for navigation.

The skill avoids fixed templates, forced sections, and course-like expansions for small questions.

## Example

When explaining large model training, use one story such as training a new employee:

- Data cleaning: preparing clean training material
- Pretraining: reading a lot and doing fill-in-the-blank practice
- Instruction tuning: learning how to follow workplace tasks
- Alignment: learning which answers are more appropriate and safer
- Evaluation: taking exams
- Deployment: going on the job
- User feedback: reviewing real work and improving next time

The explanation works when each technical point can return to the same story.
