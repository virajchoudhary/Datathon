def assist_with_disabilities(question):
    question = question.lower()

    # Mobility-related questions
    if any(keyword in question for keyword in ["wheelchair", "walker", "mobility aid", "crutches"]):
        return """Mobility aids like wheelchairs, walkers, and crutches are essential for people with mobility impairments. 
        There are options ranging from manual to electric wheelchairs, and walkers with features like hand brakes or seats for rest. 
        Consult a specialist to choose the right device for your specific needs."""

    # Hearing impairment-related questions
    elif any(keyword in question for keyword in ["hearing aid", "deaf", "hearing loss", "sign language", "cochlear implant"]):
        return """For individuals with hearing impairments, devices like hearing aids and cochlear implants can improve hearing. 
        Additionally, learning sign language can be beneficial. If you're experiencing hearing loss, it's advisable to get a hearing test from an audiologist."""

    # Vision impairment-related questions
    elif any(keyword in question for keyword in ["blind", "braille", "visual impairment", "screen reader"]):
        return """For individuals who are blind or visually impaired, tools like braille displays, screen readers, and magnifying devices can be extremely helpful. 
        Many modern devices, including smartphones, have built-in accessibility features that cater to vision impairments."""

    # Accessibility laws and rights
    elif any(keyword in question for keyword in ["disability rights", "accessibility law", "ADA", "discrimination", "workplace"]):
        return """Disability rights are protected under various laws, such as the Americans with Disabilities Act (ADA) in the US or the Equality Act in the UK. 
        These laws prohibit discrimination against people with disabilities in areas such as employment, public accommodations, and transportation. 
        Ensure that your workplace or public facilities comply with these standards to provide equitable access."""

    # Mental health and disability-related questions
    elif any(keyword in question for keyword in ["mental health", "depression", "anxiety", "PTSD", "counseling"]):
        return """Mental health is an important part of overall well-being. People with disabilities can sometimes experience conditions like anxiety, depression, or PTSD. 
        Accessing mental health counseling and therapy services can provide coping mechanisms and support. It's crucial to talk to a mental health professional if you're feeling overwhelmed."""

    # Benefits and support systems
    elif any(keyword in question for keyword in ["disability benefits", "financial aid", "social security", "government assistance"]):
        return """Disability benefits, such as financial aid or social security, are often available for those with disabilities. 
        Each country has specific programs and criteria for eligibility. You'll typically need medical documentation and may need to go through an application process to qualify."""

    # Accessibility in public spaces
    elif any(keyword in question for keyword in ["accessible parking", "public transport", "ramps", "elevator", "building accessibility"]):
        return """Public spaces are required to provide accessibility features, such as ramps, elevators, and designated accessible parking spots, under most modern accessibility laws. 
        If you find a public space lacking in accessibility, you may file a complaint with local authorities to ensure that the space complies with these laws."""

    # Assistive technology and software
    elif any(keyword in question for keyword in ["assistive technology", "voice recognition", "screen reader", "text-to-speech", "smart home devices"]):
        return """Assistive technology plays a significant role in improving accessibility. Voice recognition software, screen readers, and text-to-speech programs help those with visual or physical impairments. 
        Additionally, smart home devices can automate everyday tasks, making life easier for people with disabilities."""

    # Handling general disability-related inquiries
    elif any(keyword in question for keyword in ["disability", "accessible", "support", "help", "inclusion"]):
        return """Disability inclusion means ensuring that all individuals, regardless of their abilities, have equal access to opportunities, resources, and support. 
        If you’re seeking information on how to create more inclusive environments, consider reviewing accessibility guidelines and engaging in disability advocacy initiatives."""

    # If the question doesn't match any known category
    else:
        return "I'm sorry, I don't have an answer for that specific question. It might be best to consult with a healthcare professional or a specialist in the relevant field."

if __name__ == "__main__":
    print("Disability Support Assistant: How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Disability Support Assistant: Goodbye! Feel free to ask for help anytime.")
            break
        response = assist_with_disabilities(user_input)
        print(f"Disability Support Assistant: {response}")
