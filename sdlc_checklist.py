
print("\n=== AI-Powered SDLC Security Checklist Generator v2 ===\n")

import datetime
import json


def generate_checklist(phase):
    checklists = {
        "design": [
            "Perform threat modeling",
            "Identify data classification",
            "Define authentication mechanism",
        ],
        "build": [
            "Run static code analysis",
            "Check dependency vulnerabilities",
            "Ensure secure coding standards",
        ],
        "test": [
            "Run automated security tests",
            "Validate input sanitization",
            "Perform dynamic analysis",
        ],
        "deploy": [
            "Validate deployment scripts",
            "Run infrastructure security scan",
            "Verify secrets management",
        ],
    }
    return checklists.get(phase.lower())


def export_json(phase, checklist):
    payload = {
        "phase": phase.lower(),
        "generated_at": datetime.datetime.now().isoformat(timespec="seconds"),
        "checklist": checklist,
    }
    filename = f"checklist_{phase.lower()}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    return filename


def main():
    print("\n=== AI SDLC Security Checklist Generator ===\n")
    phase = input("Enter SDLC phase (design/build/test/deploy): ").strip()

    checklist = generate_checklist(phase)
    if not checklist:
        print("\n❌ Invalid phase entered. Please use: design/build/test/deploy")
        return

    print(f"\nSecurity Checklist for {phase.capitalize()} Phase:")
    for i, item in enumerate(checklist, 1):
        print(f"{i}. {item}")

    save = input("\nSave this as JSON? (y/n): ").strip().lower()
    if save == "y":
        filename = export_json(phase, checklist)
        print(f"✅ Saved to {filename}")


if __name__ == "__main__":
    main()


