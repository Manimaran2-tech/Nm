from nrclex import NRCLex
import matplotlib.pyplot as plt

# Plotting function
def plot_emotions(emotion_scores):
    emotions = list(emotion_scores.keys())
    scores = list(emotion_scores.values())

    plt.figure(figsize=(10, 5))
    plt.bar(emotions, scores, color='skyblue')
    plt.xlabel("Emotions")
    plt.ylabel("Scores")
    plt.title("Emotion Distribution")
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

# Analyze text and show results
def analyze_text(input_text):
    emotion = NRCLex(input_text)
    print("\nInput:", input_text)
    print("Raw Emotion Scores:", emotion.raw_emotion_scores)
    print("Top Emotions:", emotion.top_emotions)
    plot_emotions(emotion.raw_emotion_scores)

# Runtime loop
def run_emotion_analysis():
    print("=== Emotion Analyzer ===")
    while True:
        user_input = input("\nEnter a sentence (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting Emotion Analyzer.")
            break
        analyze_text(user_input)

# Start the program
if __name__ == "__main__":
    run_emotion_analysis()
