---
marp: true
---

# Trial 1: [The Yan report](https://zenodo.org/record/4028830#.X1_bxGhKg2y)

In September 2020, the above claimed to **be** scientific evidence for SARS-CoV-2 being an engineered bioweapon :fearful: Zenodo granting it a Digital Object Identifier (DOI) made the report appear credible, despite the lack of peer review.

<br>The Johns Hopkins University [made up for that lack](https://www.centerforhealthsecurity.org/our-work/pubs_archive/pubs-pdfs/2020/200921-in-response-yan.pdf) the same month, explaining why the report was unconvincing. But conspiratorial audiences :raised_eyebrow::raised_eyebrow: value neither authority, nor being pointed to tonnes of reading material (can't blame them for the latter :smile:).

<br>They do value critical thinking, which only requires that __the core claim__ be verified. Should it prove false, everything else can be dropped :woman_shrugging: What was the report's postulate, then, that sufficed for its authors to be able to seek asylum in the USA?

---

## Restriction enzymes around the spike's receptor binding motif

Mikolaj Raszek, PhD, was kind enough to elucidate, in [SARS-CoV-2 coronavirus origins alternative theories – do they hold up against science?](https://merogenomics.ca/blog/en/117/SARS-CoV-2_coronavirus_origins_alternative_theories__do_they_hold_up_against_science_Part_2), the core claim of the Yan report.

Two restriction enzymes (sequences bacteria use to slash virii to bits, repurposed by humans to glue parts of different genomes together): [EcoRI](https://www.neb.com/products/r0101-ecori#Product%20Information) and [BstEII](https://www.neb.com/products/r0162-bsteii#Product%20Information). According to Yan et al, the sequence between them allowed for targetting mammals larger than bats.
![Heart of the Yan report](https://user-images.githubusercontent.com/13955209/179063218-748bafb5-5ad1-4f32-a4da-89bd1e3e259f.png)

---

## Download the earliest known SARS-CoV-2 genome :arrow_down: (1 of 2)

<br>Yan et al's image caption cites the isolate **Wuhan-Hu-1** (isolate: a population of organisms having little genetic mixing with other organisms of the same species).

<br>![Aaa](https://user-images.githubusercontent.com/13955209/179288273-5f752b8d-1ed1-4a64-bf0d-61e9d792fe59.png)

<br>Viewing [the isolate at _NCBI Virus_](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?SeqType_s=Nucleotide&VirusLineage_ss=Severe%20acute%20respiratory%20syndrome%20coronavirus%202,%20taxid:2697049&IsolateParsed_s=Wuhan-Hu-1), the absolutely earliest accession (unique sequence identifier) is [MN908947.1](https://www.ncbi.nlm.nih.gov/nuccore/MN908947.1), collected in Dec 2019 :arrow_right: submitted 2020-01-05 :arrow_right: released 2020-01-12.

<br>That's 2 months until the World Health Organization would declare COVID-19 a pandemic ☣️ (2020-03-11).

---

## Download the earliest known SARS-CoV-2 genome :arrow_down: (2 of 2)

In the accession page, switching to the FASTA format (a text format often used for storing reference genomes) allows us to download the troublemaker's genome:

![Downloading](https://user-images.githubusercontent.com/13955209/179091431-050a1882-24e8-4591-b176-d2d905f269aa.png)

~30k bases (a base is one of `A, C, G, T`) long? What a tiny genome. A human one is 3.1 billion bases, with a single cell taking up between 3.3 GB (reference genome, a measurement standard) and 70 GB (non-reference genome) of your hard drive :see_no_evil:

---

## Are EcoRI and BstEII _actually there_? :mag::eyes:

<br>You can open the downloaded SARS-CoV-2 genome in a text editor :clipboard:, and search (`Ctrl+f` / `Cmd+f`) for the occurrences of the [EcoRI](https://www.neb.com/products/r0101-ecori#Product%20Information) sequence __GAATTC__ yourself. If you fancy a dopamine rush, __stop reading and go ahead now__ :grin:

<br>The __N__ (= whichever base) in [BstEII](https://www.neb.com/products/r0162-bsteii#Product%20Information)'s __GGTNACC__ is a tad more problematic, though. If you can locate _regular expression mode_ (look for a button marked `.*`) :crossed_fingers:, this hurdle can be cleared by inputting __GGT[ACGT]ACC__.

---

## Plotting occurences in the spike gene

You gotta give it to Yan et al: the spike gene does have EcoRI & BstEII occurences, and that's at the __exact__ coordinates specified by their team :dart: Neat :raised_hands:

<br>

| MN908947.1 spike coordinates | Yan et al's coordinates |
|--------------|:-----:|
| ![Spike genes](https://user-images.githubusercontent.com/13955209/179909322-8f79e271-2baf-4639-8db4-51f95d6db1bf.png) | ![Heart of the Yan report](https://user-images.githubusercontent.com/13955209/179063218-748bafb5-5ad1-4f32-a4da-89bd1e3e259f.png) |

---

## Plotting occurences across the whole genome

But looking at **all the genes** (instead of just the spike), one seems to find more 'genetic modifications' than Yan et al bargained for :thinking: There's even an EcoRI match in the 3' untranslated region (nothing there becomes proteins, hence little point in engineering).


![All genes](https://user-images.githubusercontent.com/13955209/179872222-cb2ecf4a-3f04-4a1e-abb5-1cc1f5e15fad.png)

---

## Is this really the restriction enzyme cornucopia? :unicorn:

[Bioinformatics Algorithms: An Active Learning Approach](https://bioinformaticsalgorithms.com/faqs/replication.html) (search for `approximation`) teaches approximating the probability of a k-mer (word of size k) occurring in a text, a certain number of times, __by random chance alone__.

Here's [the Python version](https://github.com/engelanna/verifying-sars-cov-2-origin-hypotheses/blob/master/src/probabilities/probability_of_kmer_occurring_n_times_in_text.py#L14-L23) (should you prefer it to the math equation from the link):

```python
comb(  # number of combinations
    count_of_ways_to_intersect_n_occurences_of_kmer_with_text_length
    + kmer_occurrence_count,
    kmer_occurrence_count,
)
* pow(
    self.alphabet_size,
    count_of_ways_to_intersect_n_occurences_of_kmer_with_text_length,
)
/ pow(self.alphabet_size, text_length)
```

The code's been [tested](https://github.com/engelanna/verifying-sars-cov-2-origin-hypotheses/blob/main/test/probabilities/probability_of_kmer_occurring_n_times_in_text.py), so should be reliable. Let's take it for a spin :yarn::cat:

---

https://www.citizensjournal.us/patents-prove-sars-cov-2-is-a-manufactured-virus/

Note: Yan et al measured from the beginning of the spike, the [accession page]](https://www.ncbi.nlm.nih.gov/nuccore/MN908947.1) puts that at 21579. 



---

Plotting EcoRI/BstEII occurences across just the spike 


Fatality: Occam's razor