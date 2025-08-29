"""
Chain of Thought Prompting Example

Chain of thought prompting encourages the AI to break down complex problems 
into step-by-step reasoning, showing the thought process before reaching 
a conclusion. This leads to more accurate and explainable results.
"""

def chain_of_thought_example():
    """
    Example of chain of thought prompting for travel budget calculation
    """
    
    # Chain of thought prompt: Explicit step-by-step reasoning
    prompt = """
    I need to calculate if I can afford a 7-day trip to Japan with a $2000 budget.
    Let me think through this step by step:

    Step 1: Break down the major expense categories
    - Flights: round-trip to Japan
    - Accommodation: 7 nights
    - Food: 3 meals per day for 7 days
    - Transportation: local travel within Japan
    - Activities: sightseeing and experiences
    - Miscellaneous: shopping, tips, emergency fund

    Step 2: Estimate each category
    - Flights: $800-1200 (depending on season and departure city)
    - Accommodation: $80-150 per night × 7 nights = $560-1050
    - Food: $50-80 per day × 7 days = $350-560
    - Transportation: JR Pass 7-day = $280, local transport $100 = $380
    - Activities: $300-500 for temples, museums, experiences
    - Miscellaneous: $200-300

    Step 3: Calculate total ranges
    - Minimum total: $800 + $560 + $350 + $380 + $300 + $200 = $2590
    - Maximum total: $1200 + $1050 + $560 + $380 + $500 + $300 = $3990

    Step 4: Compare with budget
    - My budget: $2000
    - Minimum estimated cost: $2590
    - Deficit: $2590 - $2000 = $590

    Conclusion: $2000 is not sufficient for a comfortable 7-day Japan trip. 
    I would need at least $2600 or should consider budget-saving options.

    Now analyze if a $1500 budget is sufficient for a 5-day trip to Thailand.
    Show your step-by-step reasoning.
    """
    
    print("Chain of Thought Prompt:")
    print(prompt)
    print("\n" + "="*50 + "\n")
    
    return prompt

def itinerary_planning_cot():
    """
    Chain of thought for optimal itinerary planning
    """
    
    prompt = """
    Plan the most efficient 3-day itinerary for Rome. Let me work through this systematically:

    Step 1: Identify must-see attractions and their locations
    - Ancient Rome area: Colosseum, Roman Forum, Palatine Hill
    - Vatican area: Vatican Museums, Sistine Chapel, St. Peter's Basilica
    - Central Rome: Pantheon, Trevi Fountain, Spanish Steps
    - Trastevere: Local neighborhood, restaurants, nightlife

    Step 2: Consider opening hours and booking requirements
    - Vatican Museums: Need advance booking, closed Sundays (except last Sunday)
    - Colosseum: Timed entry tickets, open daily
    - Many churches: Closed during lunch hours (12:30-3:30 PM)
    - Restaurants: Many closed on Mondays

    Step 3: Group attractions by proximity to minimize travel time
    - Day 1: Ancient Rome cluster (Colosseum area)
    - Day 2: Vatican area (requires full morning)
    - Day 3: Central Rome walking tour

    Step 4: Consider energy levels and optimal timing
    - Morning: High energy activities (major sights)
    - Afternoon: Lighter activities after lunch break
    - Evening: Dining and relaxation

    Step 5: Account for practical factors
    - Walking distances between sites
    - Metro/bus connections
    - Meal timing and restaurant locations
    - Rest breaks and photo opportunities

    Final optimized itinerary:
    Day 1: Colosseum (9 AM) → Roman Forum → Palatine Hill → Lunch in Monti → Pantheon → Trevi Fountain
    Day 2: Vatican Museums (8 AM) → Sistine Chapel → St. Peter's Basilica → Lunch → Castel Sant'Angelo → Evening in Borgo
    Day 3: Spanish Steps → Villa Borghese → Lunch → Trastevere exploration → Sunset at Gianicolo Hill

    Now plan a similar 4-day itinerary for Barcelona using this step-by-step approach.
    """
    
    print("Itinerary Planning Chain of Thought:")
    print(prompt)
    print("\n" + "="*50 + "\n")
    
    return prompt

def packing_decision_cot():
    """
    Chain of thought for packing decisions
    """
    
    prompt = """
    Help me decide what to pack for a 10-day trip to Iceland in March. 
    Let me think through this systematically:

    Step 1: Research destination climate and conditions
    - Iceland in March: Late winter/early spring
    - Temperature: -2°C to 4°C (28°F to 39°F)
    - Weather: Snow, rain, wind, possible storms
    - Daylight: 11-12 hours, Northern Lights still visible
    - Activities: Glacier hiking, hot springs, sightseeing

    Step 2: Consider planned activities and their requirements
    - Outdoor activities: Need waterproof, warm layers
    - Hot springs: Need swimwear, quick-dry towel
    - City exploration: Need comfortable walking shoes
    - Photography: Need weather protection for equipment
    - Fine dining: Need one nice outfit

    Step 3: Apply layering strategy for variable conditions
    - Base layer: Thermal underwear, moisture-wicking materials
    - Insulating layer: Fleece or down jacket
    - Outer layer: Waterproof and windproof shell
    - Extremities: Warm hat, waterproof gloves, wool socks

    Step 4: Consider luggage constraints and versatility
    - 10 days = need efficient packing
    - Choose items that work for multiple purposes
    - Prioritize quality over quantity for cold weather gear
    - Pack items that can be layered differently

    Step 5: Essential vs. nice-to-have items
    Essential: Waterproof boots, thermal layers, rain jacket, warm hat
    Important: Camera protection, swimwear, comfortable walking shoes
    Nice-to-have: Extra casual clothes, backup gloves

    Final packing list:
    [Detailed list would follow based on this reasoning]

    Now use this same step-by-step approach to create a packing list 
    for a 7-day summer trip to Morocco.
    """
    
    print("Packing Decision Chain of Thought:")
    print(prompt)
    
    return prompt

def travel_problem_solving_cot():
    """
    Chain of thought for solving travel problems
    """
    
    prompt = """
    My flight to Paris is delayed by 6 hours, and I'm worried about missing my hotel check-in 
    and dinner reservation. Let me work through this problem step by step:

    Step 1: Assess the immediate situation
    - Original arrival: 6 PM
    - New arrival: 12 AM (midnight)
    - Hotel check-in policy: Usually available 24/7 at major hotels
    - Dinner reservation: 8 PM (definitely missed)
    - Tomorrow's plans: 9 AM walking tour

    Step 2: Identify priority actions
    - Contact hotel to confirm late check-in
    - Cancel/reschedule dinner reservation
    - Inform tomorrow's tour operator of late arrival
    - Arrange transportation from airport at midnight
    - Consider impact on tomorrow's schedule

    Step 3: Evaluate available solutions
    Hotel: Most hotels hold reservations, but should confirm
    Dinner: Too late to make original time, but could try for late dinner
    Transportation: Metro stops at ~1 AM, taxi/Uber available 24/7
    Tomorrow: May need later start or shorter itinerary

    Step 4: Create action plan with timeline
    Immediate (now): Call hotel, cancel dinner reservation
    1 hour before landing: Confirm transportation options
    Upon arrival: Quick airport exit, direct to hotel
    Tomorrow morning: Possibly start tour later to recover

    Step 5: Identify backup options
    If hotel issues: Find 24/7 reception hotel or airport hotel
    If transportation issues: Airport shuttle or ride-share
    If tomorrow affected: Reschedule or modify itinerary

    Resolution plan:
    1. Call hotel immediately to confirm late arrival
    2. Cancel dinner, research late-night food options near hotel
    3. Book reliable airport transfer
    4. Adjust tomorrow's start time if needed
    5. Keep positive attitude - this is just a minor delay!

    Now solve this travel problem using the same reasoning approach:
    "I'm in Tokyo and my wallet with all cards and cash was stolen. 
    I have 3 days left and need to get money and continue my trip."
    """
    
    print("Travel Problem Solving Chain of Thought:")
    print(prompt)
    
    return prompt

if __name__ == "__main__":
    chain_of_thought_example()
    itinerary_planning_cot()
    packing_decision_cot()
    travel_problem_solving_cot()