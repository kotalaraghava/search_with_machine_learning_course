
Task 1:

(search_with_ml) gitpod /workspace/search_with_machine_learning_course (main) $ cut -d' ' -f1 /workspace/datasets/fasttext/labeled_queries_1000.txt | sort | uniq | wc
    387     387    9422

(search_with_ml) gitpod /workspace/search_with_machine_learning_course (main) $ cut -d' ' -f1 /workspace/datasets/fasttext/labeled_queries_10000.txt | sort | uniq | wc
     69      69    1614


Task 2:
Run 1 for min_quqries 1000:

(search_with_ml) gitpod /workspace/search_with_machine_learning_course (main) $ ~/fastText-0.9.2/fasttext supervised -input /workspace/datasets/fasttext/labeled_queries_train.txt -output query_classification
Read 0M words
Number of words:  7062
Number of labels: 387
Progress: 100.0% words/sec/thread:     218 lr:  0.000000 avg.loss:  4.114386 ETA:   0h 0m 0s

(search_with_ml) gitpod /workspace/search_with_machine_learning_course (main) $ ~/fastText-0.9.2/fasttext test query_classification.bin /workspace/datasets/fasttext/labeled_queries_test.txt 1
N       10000
P@1     0.484
R@1     0.484

(search_with_ml) gitpod /workspace/search_with_machine_learning_course (main) $ ~/fastText-0.9.2/fasttext test query_classification.bin /workspace/datasets/fasttext/labeled_queries_test.txt 3
N       10000
P@3     0.214
R@3     0.642

Run 2 with 10000 min queries:

(search_with_ml) gitpod /workspace/search_with_machine_learning_course (main) $ ~/fastText-0.9.2/fasttext test query_classification_10k.bin /workspace/datasets/fasttext/labeled_queries_test_10k.txt 1
N       10000
P@1     0.587
R@1     0.587

(search_with_ml) gitpod /workspace/search_with_machine_learning_course (main) $ ~/fastText-0.9.2/fasttext test query_classification_10k.bin /workspace/datasets/fasttext/labeled_queries_test_10k.txt 3
N       10000
P@3     0.26
R@3     0.781