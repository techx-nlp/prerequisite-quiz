# Modeling Quiz

**Estimated Completion Time:** 2 hour

This quiz assesses the student's ability to design a model according to a given dataset.

## Instructions

You are provided with a dataset of questions, each corresponding to a normed score of the question's quality (e.g. grammatical correctness, clarity, etc). Your goal is to train a model (with `train.csv`) that predicts a question's quality score, and use the model to predict the quality of a validation set of questions (presented in `test.csv`).

You will need to submit both the model's program file and the predicted quality scores as a `.csv` file.

### Output Format

A `.csv` file with one column: the predicted quality score of the question (in the exact order as the `train.csv` file).

## Notes

- The column separator in `train.csv` and `test.csv` is tab `\t` (not comma `,`)