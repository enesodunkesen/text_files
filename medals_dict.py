import csv

# When writing CSV data with a DictWriter, we have to tell it which columns to include, and which order we want to write
# If you want to skip a column, and not have it written to the file, then you have to pass 'ignore' as the argument
# for the extrasaction parameter. If you don't do that, you'll get a ValueError
# when the dictionaries contain keys that aren't listed.
medals_table = [
    {'country': 'United States', 'gold': 39, 'silver': 41, 'bronze': 33, 'rank': 1},
    {'country': 'China', 'gold': 38, 'silver': 32, 'bronze': 18, 'rank': 2},
    {'country': 'Japan', 'gold': 27, 'silver': 14, 'bronze': 17, 'rank': 3},
    {'country': 'Great Britain', 'gold': 22, 'silver': 21, 'bronze': 22, 'rank': 4},
    {'country': 'ROC', 'gold': 20, 'silver': 28, 'bronze': 23, 'rank': 5},
    {'country': 'Australia', 'gold': 17, 'silver': 7, 'bronze': 22, 'rank': 6},
    {'country': 'Netherlands', 'gold': 10, 'silver': 12, 'bronze': 14, 'rank': 7},
    {'country': 'France', 'gold': 10, 'silver': 12, 'bronze': 11, 'rank': 8},
    {'country': 'Germany', 'gold': 10, 'silver': 11, 'bronze': 16, 'rank': 9},
    {'country': 'Italy', 'gold': 10, 'silver': 10, 'bronze': 20, 'rank': 10},
    {'country': 'Canada', 'gold': 7, 'silver': 6, 'bronze': 11, 'rank': 11},
    {'country': 'Brazil', 'gold': 7, 'silver': 6, 'bronze': 8, 'rank': 12},
    {'country': 'New Zealand', 'gold': 7, 'silver': 6, 'bronze': 7, 'rank': 13},
    {'country': 'Cuba', 'gold': 7, 'silver': 3, 'bronze': 5, 'rank': 14},
    {'country': 'Hungary', 'gold': 6, 'silver': 7, 'bronze': 7, 'rank': 15},
    {'country': 'South Korea', 'gold': 6, 'silver': 4, 'bronze': 10, 'rank': 16},
    {'country': 'Poland', 'gold': 4, 'silver': 5, 'bronze': 5, 'rank': 17},
    {'country': 'Czech Republic', 'gold': 4, 'silver': 4, 'bronze': 3, 'rank': 18},
    {'country': 'Kenya', 'gold': 4, 'silver': 4, 'bronze': 2, 'rank': 19},
    {'country': 'Norway', 'gold': 4, 'silver': 2, 'bronze': 2, 'rank': 20},
    {'country': 'Jamaica', 'gold': 4, 'silver': 1, 'bronze': 4, 'rank': 21},
    {'country': 'Spain', 'gold': 3, 'silver': 8, 'bronze': 6, 'rank': 22},
    {'country': 'Sweden', 'gold': 3, 'silver': 6, 'bronze': 0, 'rank': 23},
    {'country': 'Switzerland', 'gold': 3, 'silver': 4, 'bronze': 6, 'rank': 24},
    {'country': 'Denmark', 'gold': 3, 'silver': 4, 'bronze': 4, 'rank': 25},
    {'country': 'Croatia', 'gold': 3, 'silver': 3, 'bronze': 2, 'rank': 26},
    {'country': 'Iran', 'gold': 3, 'silver': 2, 'bronze': 2, 'rank': 27},
    {'country': 'Serbia', 'gold': 3, 'silver': 1, 'bronze': 5, 'rank': 28},
    {'country': 'Belgium', 'gold': 3, 'silver': 1, 'bronze': 3, 'rank': 29},
    {'country': 'Bulgaria', 'gold': 3, 'silver': 1, 'bronze': 2, 'rank': 30},
    {'country': 'Slovenia', 'gold': 3, 'silver': 1, 'bronze': 1, 'rank': 31},
    {'country': 'Uzbekistan', 'gold': 3, 'silver': 0, 'bronze': 2, 'rank': 32},
    {'country': 'Georgia', 'gold': 2, 'silver': 5, 'bronze': 1, 'rank': 33},
    {'country': 'Chinese Taipei', 'gold': 2, 'silver': 4, 'bronze': 6, 'rank': 34},
    {'country': 'Turkey', 'gold': 2, 'silver': 2, 'bronze': 9, 'rank': 35},
    {'country': 'Greece', 'gold': 2, 'silver': 1, 'bronze': 1, 'rank': 36},
    {'country': 'Uganda', 'gold': 2, 'silver': 1, 'bronze': 1, 'rank': 36},
    {'country': 'Ecuador', 'gold': 2, 'silver': 1, 'bronze': 0, 'rank': 38},
    {'country': 'Ireland', 'gold': 2, 'silver': 0, 'bronze': 2, 'rank': 39},
    {'country': 'Israel', 'gold': 2, 'silver': 0, 'bronze': 2, 'rank': 39},
    {'country': 'Qatar', 'gold': 2, 'silver': 0, 'bronze': 1, 'rank': 41},
    {'country': 'Bahamas', 'gold': 2, 'silver': 0, 'bronze': 0, 'rank': 42},
    {'country': 'Kosovo', 'gold': 2, 'silver': 0, 'bronze': 0, 'rank': 42},
    {'country': 'Ukraine', 'gold': 1, 'silver': 6, 'bronze': 12, 'rank': 44},
    {'country': 'Belarus', 'gold': 1, 'silver': 3, 'bronze': 3, 'rank': 45},
    {'country': 'Romania', 'gold': 1, 'silver': 3, 'bronze': 0, 'rank': 46},
    {'country': 'Venezuela', 'gold': 1, 'silver': 3, 'bronze': 0, 'rank': 46},
    {'country': 'India', 'gold': 1, 'silver': 2, 'bronze': 4, 'rank': 48},
    {'country': 'Hong Kong', 'gold': 1, 'silver': 2, 'bronze': 3, 'rank': 49},
    {'country': 'Philippines', 'gold': 1, 'silver': 2, 'bronze': 1, 'rank': 50},
    {'country': 'Slovakia', 'gold': 1, 'silver': 2, 'bronze': 1, 'rank': 50},
    {'country': 'South Africa', 'gold': 1, 'silver': 2, 'bronze': 0, 'rank': 52},
    {'country': 'Austria', 'gold': 1, 'silver': 1, 'bronze': 5, 'rank': 53},
    {'country': 'Egypt', 'gold': 1, 'silver': 1, 'bronze': 4, 'rank': 54},
    {'country': 'Indonesia', 'gold': 1, 'silver': 1, 'bronze': 3, 'rank': 55},
    {'country': 'Ethiopia', 'gold': 1, 'silver': 1, 'bronze': 2, 'rank': 56},
    {'country': 'Portugal', 'gold': 1, 'silver': 1, 'bronze': 2, 'rank': 56},
    {'country': 'Tunisia', 'gold': 1, 'silver': 1, 'bronze': 0, 'rank': 58},
    {'country': 'Estonia', 'gold': 1, 'silver': 0, 'bronze': 1, 'rank': 59},
    {'country': 'Fiji', 'gold': 1, 'silver': 0, 'bronze': 1, 'rank': 59},
    {'country': 'Latvia', 'gold': 1, 'silver': 0, 'bronze': 1, 'rank': 59},
    {'country': 'Thailand', 'gold': 1, 'silver': 0, 'bronze': 1, 'rank': 59},
    {'country': 'Bermuda', 'gold': 1, 'silver': 0, 'bronze': 0, 'rank': 63},
    {'country': 'Morocco', 'gold': 1, 'silver': 0, 'bronze': 0, 'rank': 63},
    {'country': 'Puerto Rico', 'gold': 1, 'silver': 0, 'bronze': 0, 'rank': 63},
    {'country': 'Colombia', 'gold': 0, 'silver': 4, 'bronze': 1, 'rank': 66},
    {'country': 'Azerbaijan', 'gold': 0, 'silver': 3, 'bronze': 4, 'rank': 67},
    {'country': 'Dominican Republic', 'gold': 0, 'silver': 3, 'bronze': 2, 'rank': 68},
    {'country': 'Armenia', 'gold': 0, 'silver': 2, 'bronze': 2, 'rank': 69},
    {'country': 'Kyrgyzstan', 'gold': 0, 'silver': 2, 'bronze': 1, 'rank': 70},
    {'country': 'Mongolia', 'gold': 0, 'silver': 1, 'bronze': 3, 'rank': 71},
    {'country': 'Argentina', 'gold': 0, 'silver': 1, 'bronze': 2, 'rank': 72},
    {'country': 'San Marino', 'gold': 0, 'silver': 1, 'bronze': 2, 'rank': 72},
    {'country': 'Jordan', 'gold': 0, 'silver': 1, 'bronze': 1, 'rank': 74},
    {'country': 'Malaysia', 'gold': 0, 'silver': 1, 'bronze': 1, 'rank': 74},
    {'country': 'Nigeria', 'gold': 0, 'silver': 1, 'bronze': 1, 'rank': 74},
    {'country': 'Bahrain', 'gold': 0, 'silver': 1, 'bronze': 0, 'rank': 77},
    {'country': 'Saudi Arabia', 'gold': 0, 'silver': 1, 'bronze': 0, 'rank': 77},
    {'country': 'Lithuania', 'gold': 0, 'silver': 1, 'bronze': 0, 'rank': 77},
    {'country': 'North Macedonia', 'gold': 0, 'silver': 1, 'bronze': 0, 'rank': 77},
    {'country': 'Namibia', 'gold': 0, 'silver': 1, 'bronze': 0, 'rank': 77},
    {'country': 'Turkmenistan', 'gold': 0, 'silver': 1, 'bronze': 0, 'rank': 77},
    {'country': 'Kazakhstan', 'gold': 0, 'silver': 0, 'bronze': 8, 'rank': 83},
    {'country': 'Mexico', 'gold': 0, 'silver': 0, 'bronze': 4, 'rank': 84},
    {'country': 'Finland', 'gold': 0, 'silver': 0, 'bronze': 2, 'rank': 85},
    {'country': 'Botswana', 'gold': 0, 'silver': 0, 'bronze': 1, 'rank': 86},
    {'country': 'Burkina Faso', 'gold': 0, 'silver': 0, 'bronze': 1, 'rank': 86},
    {'country': "Côte d'Ivoire", 'gold': 0, 'silver': 0, 'bronze': 1, 'rank': 86},
    {'country': 'Ghana', 'gold': 0, 'silver': 0, 'bronze': 1, 'rank': 86},
    {'country': 'Grenada', 'gold': 0, 'silver': 0, 'bronze': 1, 'rank': 86},
    {'country': 'Kuwait', 'gold': 0, 'silver': 0, 'bronze': 1, 'rank': 86},
    {'country': 'Moldova', 'gold': 0, 'silver': 0, 'bronze': 1, 'rank': 86},
    {'country': 'Syria', 'gold': 0, 'silver': 0, 'bronze': 1, 'rank': 86},
]

# the easiest way(for using DictWriter) is to create a list, containing the keys that we want to include in the CSV file:
# We'll pass that list as the fieldnames argument, when we create the DictWriter.

fieldnames = ['country', 'gold', 'silver', 'bronze', 'ignore']
file_name = "country_medals.csv"

with open(file_name, "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction='ignore')
    # can exclude some keys, if you don't want those values to appear in the CSV file.
    # to do that we should change the key in fieldnames with 'ignore' and use extrasaction kwarg
    writer.writeheader()
    # If you don't call the writeheader method,you won't get the headings in the CSV file.

    # for row in medals_table:
    #     writer.writerow(row)

    # writer.writerows(sorted(return_values(medals_table)))

    # There are two ways you can use a DictWriter to write the data.
    # You can either iterate over your sequence of dictionaries, and write the data row by row,(line114)
    # or you can send the entire sequence to the writer.(line 117)

    def return_values(dictionary: dict):
        return dictionary['country']


    # When you sort things, the sorting function has to compare them, to decide what order they go in.
    # The less than operator isn't defined for dicts how would you decide if one dictionary is less than or greater ?
    # Because they can't be compared, they can't be sorted.What we have to do,
    # is create a small function that returns the value that we want to sort on.
    # The sorted function will then call that function, to get the values that can be compared.
    writer.writerows(sorted(medals_table, key=return_values))
