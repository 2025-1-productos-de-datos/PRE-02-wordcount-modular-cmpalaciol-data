import os


def write_word_counts(counter, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    ##
    # save the results using tsv format
    output_path = os.path.join(output_folder, "wordcount.tsv")
    with open("data/output/wordcount.tsv", "w", encoding="utf-8") as f:
        for key, value in counter.items():
            # write the key and vlue to tahe file
            f.write(f"{key}\t{value}\n")
