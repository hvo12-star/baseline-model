
# Storing the four baseline pipeline results from the homework prompt.
# Each dictionary keeps the pipeline name and its two main validation metrics.
pipelines = [
    {
        "pipeline": "Count + MultinomialNB",
        "accuracy": 0.6544,
        "macro_f1": 0.6259,
    },
    {
        "pipeline": "Count + LogisticRegression",
        "accuracy": 0.6228,
        "macro_f1": 0.6138,
    },
    {
        "pipeline": "TFIDF + MultinomialNB",
        "accuracy": 0.6913,
        "macro_f1": 0.6655,
    },
    {
        "pipeline": "TFIDF + LinearSVC",
        "accuracy": 0.6824,
        "macro_f1": 0.6713,
    },
]


def find_best_by_accuracy(results):
    # This function looks through all pipeline results and returns the one with the highest accuracy.
    # The code is separated this into a function so it's easier to read.
    return max(results, key=lambda x: x["accuracy"])


def find_best_by_macro_f1(results):
    # This function does the same idea as above, but now it finds the pipeline with the best macro F1.
    # Macro F1 matters a lot here because the homework says we want to avoid weak performance on minority or weak classes.
    return max(results, key=lambda x: x["macro_f1"])


def print_all_results(results):
    # This function prints every pipeline and its metrics so the reviewer can quickly see the comparison.
    print("Baseline Model Comparison")
    print("-" * 50)

    # Loop through each pipeline one at a time and print the accuracy and macro F1 in a clean format.
    for row in results:
        print(
            f"{row['pipeline']}: "
            f"accuracy={row['accuracy']:.4f}, "
            f"macro_f1={row['macro_f1']:.4f}"
        )


def print_recommendation(results):
    # This function prints a very simple recommendation summary.
    # Choosing TFIDF + LinearSVC because it has the best macro F1, and the homework says the business priority is to avoid weak performance on minority or weak classes.
    best_accuracy = find_best_by_accuracy(results)
    best_macro_f1 = find_best_by_macro_f1(results)

    # Print best model by accuracy.
    print("\nBest by accuracy:")
    print(
        f"{best_accuracy['pipeline']} "
        f"(accuracy={best_accuracy['accuracy']:.4f})"
    )

    # Print best model by macro F1.
    print("\nBest by macro F1:")
    print(
        f"{best_macro_f1['pipeline']} "
        f"(macro_f1={best_macro_f1['macro_f1']:.4f})"
    )

    # Print a short deployment recommendation.
    print("\nRecommended first model to ship:")
    print("TFIDF + LinearSVC")

    # Explain the recommendation in plain language so the output is not just numbers.
    print(
        "Reason: It has the strongest macro F1, which better matches the "
        "business goal of avoiding weak performance on minority or weaker classes."
    )


def main():
    # This is the main workflow for the script. It runs the result summary first and then prints the recommendation.
    print_all_results(pipelines)
    print_recommendation(pipelines)


if __name__ == "__main__":
    # This line tells Python to run main() only when this file is executed directly.
    # It keeps the script organized and is a standard structure in Python files.
    main()