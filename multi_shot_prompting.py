"""
Multi Shot Prompting Example

Multi-shot prompting provides multiple examples to establish a clear pattern 
and demonstrate various scenarios before asking the AI to perform a similar task.
"""

def multi_shot_example():
    """
    Example of multi-shot prompting for travel planning
    """
    
    # Multi-shot prompt: Multiple examples + new task
    prompt = """
    Here are examples of travel packing lists for different climates:

    Example 1:
    Destination: Iceland in Winter
    Climate: Cold, snowy
    Packing List:
    - Thermal underwear
    - Waterproof boots
    - Heavy winter coat
    - Wool sweaters
    - Gloves and hat
    - Camera for Northern Lights

    Example 2:
    Destination: Thailand in Summer
    Climate: Hot, humid, rainy season
    Packing List:
    - Lightweight, breathable clothing
    - Waterproof jacket
    - Comfortable walking sandals
    - Sunscreen SPF 50+
    - Insect repellent
    - Quick-dry towel

    Example 3:
    Destination: California in Spring
    Climate: Mild, occasional rain
    Packing List:
    - Light layers (t-shirts, light sweater)
    - Comfortable walking shoes
    - Light rain jacket
    - Sunglasses
    - Casual evening outfit
    - Portable phone charger

    Now create a similar packing list for Dubai in December.
    """
    
    print("Multi-Shot Prompt:")
    print(prompt)
    print("\n" + "="*50 + "\n")
    
    return prompt

def budget_planning_multi_shot():
    """
    Another multi-shot example for budget planning
    """
    
    prompt = """
    Here are budget breakdowns for different types of travelers:

    Budget Backpacker - Southeast Asia (7 days):
    - Accommodation: $140 (hostels)
    - Food: $105 (street food, local restaurants)
    - Transportation: $50 (local buses, trains)
    - Activities: $70 (temples, hiking)
    - Total: $365

    Mid-range Traveler - European Cities (7 days):
    - Accommodation: $560 (3-star hotels)
    - Food: $350 (mix of restaurants)
    - Transportation: $150 (public transport, some taxis)
    - Activities: $280 (museums, tours)
    - Total: $1,340

    Luxury Traveler - Japan (7 days):
    - Accommodation: $1,400 (5-star hotels)
    - Food: $700 (fine dining, omakase)
    - Transportation: $300 (JR Pass, taxis)
    - Activities: $500 (private tours, experiences)
    - Total: $2,900

    Now create a budget breakdown for a mid-range traveler visiting New York City for 5 days.
    """
    
    print("Budget Planning Multi-Shot:")
    print(prompt)
    
    return prompt

if __name__ == "__main__":
    multi_shot_example()
    budget_planning_multi_shot()