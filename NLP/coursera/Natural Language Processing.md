# Natural Language Processing 

> @author: Yuanhang Tang (汤远航)
>
> @e-mail: yuanhangtangle@gmail.com
>
> This is the course note of the [NLP course in Coursera](https://www.coursera.org/specializations/natural-language-processing#courses)

## Encoding

- **Vocabulary**: all the words you treat in your model of size `N`, which can be represented as a `N`dimensional array/vector `V`.
- **One-hot encoding**: Create a `N` dimensional vector for each sentence in the training set, where the element at index `i` indicates whether the word `V[i]` occurs in that sentence (`1` if it occurs, and `0` if not).
- **Problems of one-hot encoding**: 
  - long, high dimensional
  - relation of the words are lost
  - does NOT preserve the structural information of the original sentence
  - frequency of the words are lost (to solve in the next encoding method)
- **Frequency encoding**: Encode each word with it's frequency in the corpus ( for instance, in different classes in sentiment classification task). In **sentiment classification task**, we compute the **Positive frequency** and **Negative frequency** of each word in the corpus, and create a `3`dimensional vector to represent each sentence in the training set in form of `[1, sum of the positive frequency of every unique word in the sentence, sum of the negative frequency of every unique word in the sentence]`.
  - preserve the frequency information of each word;
  - does NOT preserve the structural information;
- **Preprocessing**:
  - Remove urls, punctuations, stop words (am, are, and, I, you, at, in, on, etc.), handles (@sb, etc.)
  - Stemming (transform words to its base stem), lowercasing (transform each character to its lower form)
- **Emoji**: Emotion notations are widely used in Wechat, QQ and other social APP or website. Emoji plays a important role in expressing emotion. 

----------------------------

## Vector Space

- **Vector Space**: Vector space model is used to measure the similarity of two words or documents by the frequency of the  words. A vector space is a matrix, each column of which represents a word while each row may corresponds to a word or a document.  

  - **word by word**: Given `k`, `M[i][j]` is the number of times two word `W[i]` and `W[j]` both occur in distance `k` in the same sentence in the training corpus. 

  - **word by doc**: `M[i][j]` is the number of times `W[i]` occur in document (or a group of document) `D[j]` 

    ​	Think of each row as an attribute, then **each column can be viewed as a feature vector.** If a metric is chosen, the similarity of two documents or words can be measured. For instance, `Lp` norm, cosine, etc. The cosine similarity is the same as the Euclidean distance of the normalized feature vector, each element of which is the frequency of the corresponding word.

    ​	A word by word vector space characterizes each word by a vector using the surrounding words and thus encodes each word by a vector. **A vector representation for each word is constructed when a vector space is constructed**.

  - **PCA** or other dimension reduction methods can be used to reduce the dimension of the vector space

  - **Clustering** can be done on this vector space since the columns are feature vectors. Hopefully, you may find words with similar meaning in the same or nearing cluster.

- The underlying idea of this way of word embedding is that **a word's meaning can be inferred by the surrounding words**.

---------------------

## Machine Translation via Transformation

- **Linear transformation**: If we viewed word translation as a mapping from the vector of the original word to the vector of the corresponding word, we may assume that this transformation is **linear** for convenience and simplicity. Then this task can be modeled as a supervised learning problem. 

  - **Training method**: Suppose that  a training set of the original words `X` and that of the target words `Y` are given. Each row of `X` and `Y` represents the same meaning.  Then we can minimize the following:
    $$
    \|XR-Y\|_F = \text{tr}(R^TX^TXR - 2Y^TXR + Y^TY)
    $$

  -  derivative yields the solution, assuming that $X^T X$ is invertible:
    $$
    R = (X^TX)^{-1} X^TY
    $$
    
- **Prediction method**: For a new vector $x$, $xR$ may NOT be in the target space and we may want to find out several nearing vector as candidates. **kNN** is a natural choice. A brute force search may be conducted to find the k nearest neighbors, but approximation can be introduced to accelerate this procedure. 
  
  - **locality sensitive hashing**: Usually, we wish a hash function maps nearing integers to different buckets to avoid collision. But we want to map nearby integers to the same bucket to restrict the area we search for nearest neighbors. Locality sensitive hashing is introduced to solve this problem. More specifically, we divide the space into several areas by several hyperplane, and only search for points in the same area. We can adopt several sets of hyperplanes and search for points that lie in the same area for at least one set of separating hyperplanes to improve the accuracy.  The separating hyperplanes can chosen randomly.
  - **Kd-tree**: Another way to fasten the search is to adopt Kd-tree. We may leave this for later.

----------------------

## Vector Representation of Word and Document

The idea to encode  word  or document as a **vector** makes it possible and convenient to adopt mathematical tools to attack NLP tasks. **Measure** can be introduced to compare the similarity of different words and documents. **Dimension reduction** methods can be introduced to reduce the dimension of the representation. **kNN** can be applied to search for similar words or document. 

**Representing words as  vectors is a key idea in NLP.**

-------------------

## Auto correction

Auto correction deal with misused words. There are several kinds:

- misspelled words: dear, deah, daar, etc
- contextual error: The spelling is correct, but the context is incorrect

We first deal with the first kind. The basic procedure is:

- **Locate a misspelled word**.
- **Enumerate similar words**. This can be done by compute **minimum editing distance**  between two words, and drop those that are not in the vocabulary. The remaining are the candidate words.
-  **Calculate the probability** of each word and choose the best ones. This can be done by directly compute the frequency of each candidate. A better way is to use the surrounding words to predict the probability of each word occurring in this context. We will address this issue later.

------------------

## POS tagging

part of speech tagging, or POS tagging, refers to a technique that tags the category of each word in a sentence. For example, 'see' is a verb, 'network' is a noun, etc. **Hidden Markov model** can be applied to predict the POS tag of a given word based on the previous word.

- **HMM**: Model the POS tag of a word as a hidden state and the word as a observation. Then the classic HMM model can be applied

-----------------

## Language Model

A language model models the probability of  a sentence, or the probability of a word given the previous words

- **N-gram**
A N-gram is a consecutive sequence of words. 
  - $w_i^m$ denotes $(w_i, w_{i+1}, ... , w_{i+m-1})$
  - $P(w_i^m|w_i^{m-1}) = C(w_i^m) / C(w_i^{m-1})$
  - probability of a sequence: 
    $$
    P(w_i^1) = P(w_i)\\
    P(w_i^m) = P(w_i^m | w_i^{m-1}) \times P(w_i^{m-1})
    $$
  - **Markov assumption**: The longer the sequence is, the less likely it occurs in the corpus. In fact, A long sequence may not even occur in the corpus which will cause division over zero when estimating the conditional probability. To avoid this, the **N-gram Markov assumption** states that *the probability of a word in a sequence depends only on the previous (N-1) words*. Under this assumption, the probability of a sequence can be approximated as follows:
    $$
    P(w_1^n) = P(w_1) P(w_2|w_1) P(w_3|w_1, w_2) P(w_4 | w_1, w_2, w_3) \dots P(w_n | w_{n-N+1}^{n-1})
    $$
    As a special case, under **bigram Markov assumption**, we have:
    $$
    P(w_1^n) = P(w_1) P(w_2|w_1) P(w_3|w_2) P(w_4 | w_3) \dots P(w_n | w_{n-1})
    $$
  - For consistency of notations and simplicity of computation, we want to express shorter grams by N-grams. This can be achieved by simply adding up all N-grams starting with the given shorted gram. For this purpose, we add N-1 start-of-sentence symbol `<s>` in the beginning of the sentence, and a end-of-sentence symbol `</s>` in the end of the sentence, and the sentence will look like this:
  $$
  <s>, <s>, <s>, \dots, <s>, w_1, w_2, w_3, \dots, w_n, </s>
  $$
  The probability of the sentencecan be calculated as follows:
  $$
  P(w_1^n) = P(w_1| \text{n - 1} <s>'s) P(w_2|\text{n - 2} <s>'s, w_1) P(w_3|\text{n - 3} <s>'s, w_1, w_2) \dots P(w_n |  w_{n-N+1}^{n-1})
  $$
  If we denote the first N-1 `<s>` as $w_{-(N-2)}, w_{-(N-3)}, \dots, w_{-1}, w_0$, then we have:
  $$
  P(w_1^n) = \prod_{i = 1}^n P(w_i |  w_{i-N+1}^{i-1})\\
  = \prod_{i = 1}^n \frac{P(w_{i-N+1}^{i})}{\sum_{c \in V} P(w_{i-N+1}^{i-1}, c)}
  $$

  - To implement the N-gram model, you can build a matrix whose rows are all (N-1)-grams and columns are the whole vocabulary, with each element denoting the occurring times. Then any conditional probability in the forementioned formula can be evaluated by the dividing the corresponding element with the row sum. To avoid numerical underflow, we can take logarithm and convert product to sum.