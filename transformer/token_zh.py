import jieba


def tokenize(line):
    seg_list = jieba.cut(line, cut_all=False)
    return " ".join(seg_list)

MULTIUN_PATH = "corpora/MultiUN.en-zh.zh"

tokenized_lines = []
print("Preprocessing Data...")
with open(MULTIUN_PATH, encoding='utf8') as file:
    for line in file:
        if len(tokenized_lines) % 100000 == 0:
            print("Finish processing " + str(len(tokenized_lines)) + " lines.")
        tokenized_lines.append(tokenize(line.strip()))

print("Writing to file...")
with open(MULTIUN_PATH + "_processed", mode = 'w', encoding='utf8') as file:
    for line in tokenized_lines:
        file.write("%s\n" % line)
