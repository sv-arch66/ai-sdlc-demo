
print("\n=== AI-Powered SDLC Security Checklist Generator v2 ===\n")

def generate_checklist(phase):
    checklists = {
        "design": [
            "Perform threat modeling",
            "Identify data classification",
            "Define authentication mechanism"
        ],
        "build": [
            "Run static code analysis",
            "Check dependency vulnerabilities",
            "Ensure secure coding standards"
        ],
        "test": [
            "Run automated security tests",
            "Validate input sanitization",
            "Perform dynamic analysis"
        ],
        "deploy": [
            "Validate deployment scripts",
            "Run infrastructure security scan",
            "Verify secrets management"
        ]
    }

    return checklists.get(phase.lower(), ["Phase not found"])


if __name__ == "__main__":
    phase = input("Enter SDLC phase (design/build/deploy): ")
    items = generate_checklist(phase)

    print(f"\nSecurity Checklist for {phase.capitalize()} Phase:")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")

        