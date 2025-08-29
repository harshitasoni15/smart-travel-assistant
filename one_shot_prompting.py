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
    - Afternoon: St. Peter's Basilica (1 hour)
    - Evening: Gelato at Piazza Navona

    Now create a similar 2-day itinerary for Barcelona, Spain.
    """
    
    print("One-Shot Prompt:")
    print(prompt)
    print("\n" + "="*50 + "\n")
    
    return prompt

def restaurant_recommendation_one_shot():
    """
    Another one-shot example for restaurant recommendations
    """
    
    prompt = """
    Example restaurant recommendation:
    
    Restaurant: Le Comptoir du Relais
    Location: Paris, France
    Cuisine: French Bistro
    Price Range: €€€
    Must-try: Duck confit, French onion soup
    Atmosphere: Cozy, traditional Parisian bistro
    Reservation: Recommended
    
    Now provide a similar recommendation for a restaurant in Tokyo, Japan.
    """
    
    print("Restaurant Recommendation One-Shot:")
    print(prompt)
    
    return prompt

if __name__ == "__main__":
    one_shot_example()
    restaurant_recommendation_one_shot()