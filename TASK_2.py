import matplotlib.pyplot as plt
import math

def draw_tree(ax, x, y, length, angle, level):
    if level == 0:
        return
    
    x_new = x + length * math.cos(math.radians(angle))
    y_new = y + length * math.sin(math.radians(angle))
    
    ax.plot([x, x_new], [y, y_new], color='brown')
    
    # Calculate new lengths and angles for the branches
    new_length = length * 0.7
    left_angle = angle + 45
    right_angle = angle - 45
    
    # Recursively draw the left and right branches
    draw_tree(ax, x_new, y_new, new_length, left_angle, level - 1)
    draw_tree(ax, x_new, y_new, new_length, right_angle, level - 1)

def main():
    # Get user input for recursion level
    recursion_level = int(input("Enter the recursion level: "))
    
    # Setup the plot
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Initial parameters for the tree
    initial_length = 100
    initial_angle = 90
    
    # Draw the tree
    draw_tree(ax, 0, 0, initial_length, initial_angle, recursion_level)
    
    # Display the plot
    plt.show()

if __name__ == "__main__":
    main()
