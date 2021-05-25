# Circulo Health - Machine Learning Test

## Introduction

For the current step of the interview process, we'd like to have you
write some code. We've attempted to keep the problem statement small
and up for interpretation, so please do not feel the need to spend
too much time.

If you have any questions please email us and we will get back to you.

If the problem statement doesn't specify something or is ambiguous,
it is up to you to make an assumption.

Please include a README.md file with your submission including a description of
your approach to solving the problem.

What we're looking for is a solution that is representative of how you would
tackle and write code for a real project. This can include tests, libraries,
anything you might use day to day, but make sure it can be built and compiled
without too much effort.

When you are finished, please compress your code as a tarball:

`tar zcvf code.tgx code-dir`

or as a gitbundle:

`GIT_DIR=code-dir/.git git bundle create code.gitbundle --all`

Send the file via email back to your recruiter (if small enough) or upload to
Google Drive/Dropbox/OneDrive and send an accessible link.

## Problem

For the given dataset `heart_attack_dataset.cvs`:

1. Show and potential relation between the `had_heart_attack` feature and other
variables (i.e. using graphs).
2. Using the dataset, build a model to predict "possibility of `had_heart_attack`":
   - Choose a proper performance metric to assess the effectiveness of your
model to predict the `had_heart_attack` variable.
   - Provider the ROC curve and explain the performance of the developed model
with respect to the ROC curve
   - Please explain other potential strategies that would have helped you to
build a model with better performance

Attribute Information:

1. `gender`: "Male", "Female", or "Other"
2. `age`: age of the patient
3. `hypertension`: 0 if the patient doesn't have hypertension, 1 if the patient
has hypertension.
4. `high_cholesterol`: 0 if the patient doesn't have high cholesterol, 1 if the
patient has high cholesterol
5. `ever_married`: "No" or "Yes"
6. `work_type`: "children", "Govt_job", "Never_worked", "Private" or "Self-employed"
7. `residence_type`: "Rural" or "Urban"
8. `avg_glucose_level`: average glucose level in blood
9. `bmi`: body mass index
10. `smoking_status`: "formerly smoked", "never smoked", "smokes", or "Unknown".
*Note: "Unknown" in smoking_status means that the information is unavailable for 
this patient*
11. `had_heart_attack`: 1 if the patient had a heart attack, or 0 if not

## Rubric/Evaluation Criteria

The main thing we are looking for from your solution is implementing enough code
and analysis to demonstrate expertise with domain modeling, data analysis, and
machine learning.

When writing your README.md we stress that you express your thoughts behind
choices you made, assumptions you made, and your overall plan of attack.
For example, you can use a multitude of different models and classifiers
for a dataset like k-nearest neighbors, naive bayes, etc. We do not
consider any of these better than the others, but want to know why you
chose that approach.

As a general rule of thumb, we want to see more structure than what the
problem might require. We understand that keeping code simple is important,
and we don't want to add an excessive amount of requirements that it would
take too much time to complete.

Overall, we will be evaluating on the following:

- README
- Data Modeling
- Conclusions from Data Analysis/Machine Learning
- Code Readability
- Code Structure
