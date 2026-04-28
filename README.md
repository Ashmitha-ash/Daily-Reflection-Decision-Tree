Daily Reflection Decision Tree
Project Overview
This project is a deterministic decision tree built for the Deep Thought Culture Tech Ventures recruitment assignment. It is designed to help users scientifically reflect on their daily productivity by following a strict logical path to actionable outcomes.

Key Features
Deterministic Logic: Unlike probabilistic models, this tree uses a fixed "If-Then" structure to eliminate ambiguity in decision-making.


Scientific Execution: The outcomes are not generic; they focus on specific interventions like "Re-prioritizing with a lead" or "Energy peak identification".  

AI-Assisted with Guardrails: This tool was developed using AI with strict negative prompting to ensure the output remained objective and free from "hallucinations" or vague emotional advice.

Logic Flow

Primary Goal Check: Did the user finish their top priority?   


Obstacle Classification: Was the barrier Internal (mindset/habit) or External (process/environment)?   


Actionable Result: A specific strategy is provided based on the exact path taken.  

Technical Implementation
Language: Python
Structure: Nested conditional statements ensuring 100% predictability in results.

graph TD
    %% Axis 1: Locus of Control
    START((Start Reflection)) --> A1Q1{Did you feel in control today?}
    A1Q1 -- Yes: Victor --> A1R1[Reflection: You recognized your agency]
    A1Q1 -- No: Victim --> A1R2[Reflection: Even in tough times, you make choices]
    
    %% Bridge 1
    A1R1 --> B1[Bridge: Shifting to Contribution]
    A1R2 --> B1
    
    %% Axis 2: Orientation
    B1 --> A2Q1{Did you help a teammate?}
    A2Q1 -- Yes: Contribution --> A2R1[Reflection: Giving builds value]
    A2Q1 -- No: Entitlement --> A2R2[Reflection: Focus on what you can provide]
    
    %% Bridge 2
    A2R1 --> B2[Bridge: Shifting to Radius]
    A2R2 --> B2
    
    %% Axis 3: Radius of Concern
    B2 --> A3Q1{Who benefited from your work?}
    A3Q1 -- The Team/User --> SUM[Summary: Altrocentric approach]
    A3Q1 -- Just Me --> SUM[Summary: Self-centric focus detected]
    
    SUM --> END((End Session))
