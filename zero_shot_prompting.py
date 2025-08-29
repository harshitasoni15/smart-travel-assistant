"""
Zero Shot Prompting Example

Zero-shot prompting involves asking the AI to perform a task without providing 
any examples or prior context about how to do it.
"""

def zero_shot_example():
    """
    Example of zero-shot prompting for travel assistance
    """
    
    # Zero-shot prompt: Direct task without examples
    prompt = """
    You are a travel assistant. Plan a 3-day itinerary for Paris, France. 
    Include must-see attractions, recommended restaurants, and transportation tips.
    """
    
    print("Zero-Shot Prompt:")
    print(prompt)
    print("\n" + "="*50 + "\n")
    
    # Expected behavior: AI should generate a complete Paris itinerary
    # without any examples or templates provided
    
    return prompt

def travel_recommendation_zero_shot():
    """
    Another zero-shot example for travel recommendations
    """
    
    prompt = """
    Recommend the best time to visit Tokyo, Japan. 
    Consider weather, festivals, and tourist crowds.
    """
    
    print("Travel Recommendation Zero-Shot:")
    print(prompt)
    
    return prompt

if __name__ == "__main__":
    zero_shot_example()
    travel_recommendation_zero_shot()