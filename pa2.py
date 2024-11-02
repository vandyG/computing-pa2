# %%

from typing import List


def filter_popular(reacts_2D: List[List[int]], names: List[str], threshold: int) -> List[str]:
    """Filters a list of names to only include those whose total engagement (likes, etc.) meets a given threshold.

    Args:
        reacts_2D: A 2D list where each sublist represents the engagement counts (likes, etc.) for a corresponding name.
        names: A list of names corresponding to the engagement data in `reacts_2D`.
        threshold: The minimum total engagement count required for a name to be considered "popular".

    Returns:
        A new list containing only the names from `names` whose total engagement count in `reacts_2D` is greater than or equal to `threshold`.
    """
    # Initialize a list to store popular users
    popular_users = []

    # Iterate over each user's engagement data and name
    for i in range(len(reacts_2D)):
        # Calculate the sum of engagements for each user
        total_engagement = 0

        for count in reacts_2D[i]:
            total_engagement += count
        # Check if the total engagement meets the threshold

        if total_engagement >= threshold:
            popular_users.append(names[i])

    return popular_users


# %%
filter_popular(
    [[4, 9, 6, 5], [1, 2, 3, 5, 8], [17, 2, 9]], ["crazy_guy", "solid321", "amicoolyet"], 22
)  # ['crazy_guy', 'amicoolyet']

# %%
filter_popular(
    [[4, 9, 6, 5], [1, 2, 3, 5, 8], [17, 2, 9]], ["crazy_guy", "solid321", "amicoolyet"], 15
)  # ['crazy_guy', 'solid321', 'amicoolyet']

# %%
filter_popular(
    [[31], [22, 1, 1], [2, 2, 11, 65]], ["alien", "tomato2", "simon23"], 50
)  # ['simon23']

# %%
filter_popular([[31], [22, 1, 1], []], ["alien", "tomato2", "simon23"], 30)  # ['alien']

# %%

filter_popular([], ["alien", "tomato2", "simon23"], 50)  # []


# %%
def gather_engagement(names: List[str], reacts, grouping):
    """Groups engagement data (likes, comments, etc.) for each user based on a grouping list.

    Args:
        names: A list of user names.
        reacts: A list containing engagement data (likes, comments, etc.) for all users.
        grouping: A list of integers representing the number of engagement data points for each user.

    Returns:
        A list of lists, where each sublist represents a user and contains their name followed by their grouped engagement data.
    """
    # Initialize a list to store grouped engagement data
    grouped_engagements = []
    index = 0  # To keep track of reacts list index

    for i in range(len(names)):
        user_data = [names[i]]
        # Get the number of engagement data counts for each user

        for _ in range(grouping[i]):
            user_data.append(reacts[index])
            index += 1

        grouped_engagements.append(user_data)

    return grouped_engagements


# %%
gather_engagement(
    ["crazy_guy", "solid321", "amicoolyet"], [4, 9, 6, 5, 1, 2, 3, 5, 8, 17, 2, 9], [4, 5, 3]
)  # [['crazy_guy', 4, 9, 6, 5], ['solid321', 1, 2, 3, 5, 8], ['amicoolyet', 17, 2, 9]]
# %%
gather_engagement(
    ["crazy_guy", "solid321", "amicoolyet"], [4, 9, 6, 5, 1, 2, 3, 5, 8, 17, 2, 9], [2, 1, 9]
)  # [['crazy_guy', 4, 9], ['solid321', 6], ['amicoolyet', 5, 1, 2, 3, 5, 8, 17, 2, 9]]

# %%
gather_engagement(
    ["butter12", "helloworld"], [40, 3, 35, 7], [0, 4]
)  # [['butter12'], ['helloworld', 40, 3, 35, 7]]


# %%
def clear_zeros(reacts_2D):
    # Initialize a list to store cleared engagement data
    cleared_reacts = []

    for user_data in reacts_2D:
        cleaned_data = []
        # Remove zeros from each user's data

        for value in user_data:
            if value != 0:
                cleaned_data.append(value)

        # Add only non-empty lists
        if cleaned_data:
            cleared_reacts.append(cleaned_data)

    return cleared_reacts
