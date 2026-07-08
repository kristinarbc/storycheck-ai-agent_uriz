import os
from agent.workflow import build_workflow
from services.loader import load_stories_from_file, get_manual_story


def save_report(state, filename="output/report.md"):
    os.makedirs("output", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# StoryCheck AI Agent - Report\n\n")
        f.write(f"## Original User Story\n{state['story']}\n\n")
        f.write(f"## Analysis\n{state['analysis']}\n\n")
        f.write(f"## Acceptance Criteria\n{state['acceptance_criteria']}\n\n")
        f.write(f"## Test Cases\n{state['test_cases']}\n\n")
        f.write(f"## Risk Assessment\n{state['risks']}\n\n")
        f.write(f"## Recommendations\n{state['recommendations']}\n\n")
    print(f"Report sacuvan: {filename}")


def main():
    print("1 - Ucitaj iz data/stories.json")
    print("2 - Unesi rucno")
    choice = input("Izbor: ")

    if choice == "1":
        stories = load_stories_from_file()
        print(f"Ucitano {len(stories)} story-ja. Koji index? (0, 1, 2...)")
        idx = int(input("Index: "))
        story = stories[idx]
    else:
        story = get_manual_story()

    workflow = build_workflow()
    initial_state = {
        "story": story,
        "analysis": "",
        "acceptance_criteria": "",
        "test_cases": "",
        "risks": "",
        "recommendations": ""
    }

    result = workflow.invoke(initial_state)
    save_report(result)


if __name__ == "__main__":
    main()