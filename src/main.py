# main.py

from pipeline import multi_persona_pipeline

def main():
    user_prompt = "How can our city improve environmental sustainability?"

    # Pass {"question": ...} so pipeline_func can forward it to each persona agent
    context = multi_persona_pipeline({"question": user_prompt})

    print("\n--- FINAL OUTPUT ---")
    print(context.result)

if __name__ == "__main__":
    main()
