"""
One Shot Prompting Example

One-shot prompting provides exactly one example to demonstrate the desired 
output format or behavior before asking the AI to perform a similar task.
"""

def one_shot_example():
    """
    Example of one-shot prompting for travel planning
    """
    
    # One-shot prompt: One example + new task
    prompt = """
    Here's an example of a travel itinerary format:

    Example:
    City: Rome, Italy
    Duration: 2 days
    Day 1:
    - Morning: Visit Colosseum (2 hours)
    - Afternoon: Explore Roman Forum (1.5 hours)
    - Evening: Dinner at Trastevere district
    Day 2:
    - Morning: Vatican Museums and Sistine Chapel (3 hours)
    - Afternoon