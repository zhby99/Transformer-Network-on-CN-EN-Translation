from transformer.hyperparams import Hyperparams as hp

TRAIN_SET_SIZE = 200000
TEST_SET_SIZE = 1000


def split_data(file_path):
    train_set = []
    test_set = []
    with open(file_path, encoding='utf8') as file:
        line_num = 0
        for line in file:
            if line_num < TEST_SET_SIZE:
                test_set.append(line)
            elif line_num < TRAIN_SET_SIZE + TEST_SET_SIZE:
                train_set.append(line)
            else:
                break
            line_num += 1
    with open(file_path + "_test", mode='w', encoding='utf8') as file:
        for line in test_set:
            file.write("%s" % line)

    with open(file_path + "_train", mode='w', encoding='utf8') as file:
        for line in train_set:
            file.write("%s" % line)


if __name__ == '__main__':
    split_data(hp.source)
    split_data(hp.target)
    print("Done")
