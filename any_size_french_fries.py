# Original price and tax rates
# The original_price variable is set to 1.49, representing the initial price of an item before any adjustments or taxes are applied.
# This value serves as the baseline for calculating the final price after tax.
# The tax_rate_original variable is assigned a value of 0.08, indicating an 8% tax rate applicable to the original price.
# This tax rate determines the additional amount to be added to the original price to account for taxes, ensuring that the total
# price reflects the tax percentage.
original_price = 1.49
tax_rate_original = 0.08  # 8% tax rate for original price


# Desired ratio for price to total price with tax
# The optimal_ratio variable is calculated as 0.99 divided by 1.07, resulting in approximately 0.9252.
# This ratio ensures that when the price of an item is added to the 8% tax rate (1.07), the total
# price paid by the customer is a whole dollar ($1.07). This pricing strategy simplifies transactions
# and makes the total price more appealing to customers. It also helps businesses avoid dealing with
# small change, enhancing customer satisfaction and streamlining pricing structures.
optimal_ratio = 0.99 / 1.07  # The desired ratio for price to total price with tax


# Function to calculate the ratio based on the adjusted price
# This function calculates the ratio of the adjusted price to the total price with tax.
# It takes two parameters: 'price', which represents the adjusted price of the item,
# and 'tax_rate', which is the tax rate applicable to the price.
def calculate_adjusted_ratio(price, tax_rate):
    # Calculate the total price with tax by adding the price to the tax amount (price * tax_rate)
    total_price_with_tax = price + (price * tax_rate)
    # Calculate the ratio of the price to the total price with tax
    # This ratio represents the portion of the total price that is the actual price of the item,
    # excluding the tax component. It helps in understanding the impact of taxes on the price.
    return price / total_price_with_tax


# Start at the original price and iterate downwards by $0.01 until we find the matching ratio.
# This process ensures that we explore all possible price adjustments, starting from the original price and moving downwards in increments of $0.01.
# By systematically decrementing the price, we can evaluate the impact of each adjustment on the price-to-total-price ratio with tax.
# This iterative approach allows us to identify the optimal price point where the ratio closely matches the desired optimal ratio.
# Once we find a price that meets this criterion, we stop the iteration, as we have identified a price that achieves the desired pricing goal.
adjusted_price = original_price
while adjusted_price >= 0:

    # Iterate over possible adjustments from $0.01 to the original price.
    # This loop allows us to consider adjustments ranging from $0.01 to the full original price.
    # By incrementing the adjustment value in small increments, we can explore a wide range of possible price reductions.
    # Each iteration represents a potential adjustment to the original price, allowing us to evaluate the impact of various price changes.
    # This iterative process helps us find the optimal price that maximizes the ratio of the price to the total price with tax.


    for x in range(1, int(original_price * 100)):
        # Convert adjustment to dollars
        adjustment = x / 100
        # Calculate the new adjusted price
        new_price = adjusted_price - adjustment

        # Calculate the ratio for the new adjusted price.
        # This step computes the ratio between the adjusted price and the total price including tax.
        # The ratio indicates the proportion of the price that is not attributable to tax.
        # By comparing this ratio to the optimal ratio, we can determine how close the adjusted price is to the desired price point.
        # This calculation is crucial for identifying the adjusted price that best aligns with our pricing optimization goal.
        ratio = calculate_adjusted_ratio(new_price, tax_rate_original)

        # Check if the ratio is close to the optimal ratio.
        # This step evaluates whether the calculated ratio for the adjusted price is near the desired optimal ratio.
        # The optimal ratio represents the ideal proportion of the price to the total price with tax.
        # By checking for proximity to this optimal ratio, the algorithm identifies adjusted prices that align closely with the desired pricing structure.
        # This comparison helps in selecting the adjusted price that achieves the goal of maximizing profit while maintaining an attractive price point for customers.
        if abs(ratio - optimal_ratio) < 0.001:

            # Print the adjusted price and the calculated ratio.
            # This step displays the adjusted price and the corresponding calculated ratio.
            # Printing these values provides visibility into the process of finding the optimal price adjustment.
            # It allows for easy verification of the algorithm's calculations and helps in understanding how different adjustments affect the ratio.
            # This information is crucial for analyzing the results and determining the best pricing strategy for maximizing profit.
            print(f"Adjusted price: ${new_price:.2f}, Adjusted ratio: {ratio:.2f}")
            break
    else:

        # Decrement the adjusted price by $0.01.
        # This action reduces the adjusted price by one cent in each iteration of the loop.
        # By decreasing the price incrementally, the algorithm systematically explores different price points to find the optimal adjustment.
        # This step ensures that the algorithm checks a range of prices below the original price, seeking the best price that maximizes profit.
        # The decrementing process continues until the optimal price adjustment is found or until the adjusted price reaches zero.
        adjusted_price -= 0.01
        continue
    break

# Print the success message.
# This message indicates that the algorithm has successfully found an adjusted price that matches the desired ratio.
# It serves as a signal that the optimization process has completed and that the algorithm has achieved its objective.
# The success message provides feedback to the user or developer, indicating that the algorithm has executed as intended.
# This step concludes the algorithm's execution, informing the user of the final result and indicating that the program can terminate.
# The message reassures the user that the algorithm has completed its task successfully.
print("Success!")
