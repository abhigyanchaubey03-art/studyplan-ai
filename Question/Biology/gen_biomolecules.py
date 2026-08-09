import json

questions = []

def add(id, difficulty, question, options, answer, why_correct, why_others_wrong, concept_recap, ncertRef, qtype="Practice", year=None):
    q = {
        "id": id, "type": qtype, "difficulty": difficulty, "question": question,
        "options": options, "answer": answer, "ncertRef": ncertRef,
        "solution": {"why_correct": why_correct, "why_others_wrong": why_others_wrong, "concept_recap": concept_recap}
    }
    if year: q["year"] = year
    questions.append(q)

# ============ EASY (15) ============
add("bm-e-01","Easy","Which of the following is a monosaccharide?",
    ["Sucrose","Glucose","Starch","Cellulose"],"B",
    "Glucose is a simple sugar (monosaccharide) that cannot be hydrolyzed into a simpler carbohydrate.",
    "Sucrose is a disaccharide (glucose + fructose); starch and cellulose are polysaccharides made of many glucose units.",
    "Carbohydrates are classified as monosaccharides, oligosaccharides (2-10 units), and polysaccharides based on the number of sugar units.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-e-02","Easy","Proteins are polymers of:",
    ["Nucleotides","Amino acids","Fatty acids","Monosaccharides"],"B",
    "Proteins are long chains (polymers) of amino acids linked by peptide bonds.",
    "Nucleotides are the monomers of nucleic acids; fatty acids are components of lipids; monosaccharides are the monomers of carbohydrates.",
    "There are 20 standard amino acids that combine in various sequences to form the vast diversity of proteins.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-e-03","Easy","Which bond links amino acids together in a protein chain?",
    ["Glycosidic bond","Peptide bond","Phosphodiester bond","Hydrogen bond"],"B",
    "Amino acids are joined by peptide bonds, formed between the carboxyl group of one amino acid and the amino group of the next.",
    "Glycosidic bonds link sugar units; phosphodiester bonds link nucleotides in nucleic acids; hydrogen bonds stabilize secondary/tertiary structure but don't form the primary chain.",
    "Peptide bond formation is a dehydration (condensation) reaction, releasing a water molecule.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-e-04","Easy","DNA and RNA are examples of which class of biomolecule?",
    ["Carbohydrates","Lipids","Nucleic acids","Proteins"],"C",
    "DNA and RNA are nucleic acids, polymers built from nucleotide monomers.",
    "They are not carbohydrates, lipids, or proteins, though they do contain a sugar component (deoxyribose/ribose) as part of their nucleotide structure.",
    "Nucleic acids store and transmit genetic information; DNA is typically double-stranded, RNA usually single-stranded.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-e-05","Easy","Which of the following is NOT a nitrogenous base found in DNA?",
    ["Adenine","Uracil","Cytosine","Guanine"],"B",
    "Uracil is found in RNA, not DNA — in DNA, thymine takes its place.",
    "Adenine, cytosine, and guanine are all found in both DNA and RNA.",
    "DNA bases: Adenine, Thymine, Guanine, Cytosine. RNA bases: Adenine, Uracil, Guanine, Cytosine.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-e-06","Easy","Enzymes are chemically composed mostly of:",
    ["Carbohydrates","Lipids","Proteins","Nucleic acids"],"C",
    "Most enzymes are proteins that act as biological catalysts, speeding up biochemical reactions.",
    "While some RNA molecules (ribozymes) have catalytic activity, the vast majority of enzymes are protein-based, not carbohydrates, lipids or general nucleic acids.",
    "Enzymes lower the activation energy of reactions without being consumed, and their activity depends on their 3D protein structure.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-e-07","Easy","Which of the following is a storage polysaccharide in plants?",
    ["Cellulose","Chitin","Starch","Peptidoglycan"],"C",
    "Starch is the primary storage polysaccharide in plants, stored in amyloplasts as granules.",
    "Cellulose is a structural polysaccharide (cell wall); chitin forms fungal walls/insect exoskeletons; peptidoglycan forms bacterial cell walls.",
    "Starch consists of amylose (unbranched) and amylopectin (branched) chains of glucose units.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-e-08","Easy","The basic building block (monomer) of nucleic acids is:",
    ["Amino acid","Nucleotide","Fatty acid","Monosaccharide"],"B",
    "Nucleotides, each composed of a nitrogenous base, a pentose sugar, and a phosphate group, are the monomers of nucleic acids.",
    "Amino acids build proteins; fatty acids are lipid components; monosaccharides build carbohydrates — none are nucleic acid monomers.",
    "A nucleotide = nitrogenous base + pentose sugar + phosphate group; a nucleoside lacks the phosphate.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-e-09","Easy","Which of these is a lipid?",
    ["Glycogen","Triglyceride","Hemoglobin","Ribose"],"B",
    "Triglycerides (fats/oils) are lipids composed of glycerol and three fatty acid chains.",
    "Glycogen is a polysaccharide (carbohydrate storage in animals); hemoglobin is a protein; ribose is a monosaccharide sugar.",
    "Lipids are a diverse group including fats, oils, phospholipids, and steroids, generally insoluble in water.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-e-10","Easy","Which element is present in proteins but typically absent in carbohydrates and lipids?",
    ["Carbon","Hydrogen","Nitrogen","Oxygen"],"C",
    "Nitrogen is a characteristic element of amino acids (in the amino group) and thus proteins, generally absent in simple carbohydrates and lipids.",
    "Carbon, hydrogen, and oxygen are present in carbohydrates, lipids, and proteins alike.",
    "Proteins also often contain sulfur (in cysteine/methionine); nucleic acids contain nitrogen and phosphorus.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-e-11","Easy","Cellulose is a polymer of which monosaccharide?",
    ["Fructose","Galactose","Glucose","Ribose"],"C",
    "Cellulose is a straight-chain polysaccharide made entirely of beta-glucose units linked together.",
    "Fructose, galactose, and ribose are not the monomer units of cellulose.",
    "The beta-linkages in cellulose make it indigestible by most animals (lacking cellulase), unlike starch's alpha-linkages.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-e-12","Easy","Which of the following best describes a 'primary structure' of a protein?",
    ["The 3D folded shape","The linear sequence of amino acids","The association of multiple polypeptide chains","The alpha-helix/beta-sheet pattern"],"B",
    "Primary structure refers to the specific linear sequence of amino acids joined by peptide bonds in a polypeptide chain.",
    "3D folded shape describes tertiary structure; multiple chain association describes quaternary structure; alpha-helix/beta-sheet patterns describe secondary structure.",
    "Protein structure hierarchy: primary (sequence) → secondary (local folding) → tertiary (3D shape) → quaternary (multi-subunit assembly).",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-e-13","Easy","Which vitamin deficiency causes scurvy?",
    ["Vitamin A","Vitamin C","Vitamin D","Vitamin K"],"B",
    "Vitamin C (ascorbic acid) deficiency causes scurvy, characterized by bleeding gums and poor wound healing due to impaired collagen synthesis.",
    "Vitamin A deficiency causes night blindness; Vitamin D deficiency causes rickets; Vitamin K deficiency impairs blood clotting.",
    "Vitamins are organic micronutrients required in small amounts; some are water-soluble (B, C), others fat-soluble (A, D, E, K).",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-e-14","Easy","Which of the following is a fat-soluble vitamin?",
    ["Vitamin B1","Vitamin C","Vitamin A","Vitamin B12"],"C",
    "Vitamin A is fat-soluble and stored in the liver, along with vitamins D, E, and K.",
    "Vitamin B1, Vitamin C, and Vitamin B12 are water-soluble vitamins that are generally not stored long-term in the body.",
    "Fat-soluble vitamins (A, D, E, K) require dietary fat for absorption and can accumulate to toxic levels if oversupplemented.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-e-15","Easy","Which of the following is an example of a disaccharide?",
    ["Glucose","Maltose","Glycogen","Chitin"],"B",
    "Maltose is a disaccharide composed of two glucose units joined by a glycosidic bond.",
    "Glucose is a monosaccharide; glycogen and chitin are polysaccharides.",
    "Common disaccharides: sucrose (glucose+fructose), lactose (glucose+galactose), maltose (glucose+glucose).",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

# ============ MEDIUM (15) ============
add("bm-m-01","Medium","Which type of bond primarily stabilizes the alpha-helix secondary structure of proteins?",
    ["Peptide bonds between distant residues","Hydrogen bonds between backbone C=O and N-H groups","Disulfide bonds between cysteines","Ionic bonds between charged side chains"],"B",
    "The alpha-helix is stabilized by regular hydrogen bonding between the carbonyl oxygen (C=O) of one amino acid and the amide hydrogen (N-H) of another, four residues ahead in the chain.",
    "Peptide bonds form the primary backbone, not the helical stabilization; disulfide and ionic bonds contribute more to tertiary structure stability, not the core secondary helix pattern.",
    "Secondary structures (alpha-helix, beta-sheet) arise from regular, repeating hydrogen bonding patterns along the polypeptide backbone.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-m-02","Medium","Which of the following best distinguishes RNA from DNA structurally?",
    ["RNA has thymine, DNA has uracil","RNA is double-stranded, DNA is single-stranded","RNA has ribose sugar, DNA has deoxyribose sugar","RNA lacks phosphate groups"],"C",
    "RNA contains ribose sugar (with a hydroxyl at the 2' carbon), while DNA contains deoxyribose (lacking that hydroxyl) — this is a key structural distinction.",
    "It's DNA that has thymine and RNA that has uracil (reversed in the option); DNA is typically double-stranded, RNA single-stranded (reversed); both RNA and DNA have phosphate groups.",
    "Structural DNA vs RNA differences: sugar (deoxyribose vs ribose), base (thymine vs uracil), and strandedness (double vs single, generally).",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-m-03","Medium","Denaturation of a protein primarily affects its:",
    ["Primary structure (amino acid sequence)","Secondary, tertiary, and quaternary structure, not primary sequence","Molecular weight","Amino acid composition"],"B",
    "Denaturation disrupts the hydrogen bonds, ionic interactions, and other weak forces maintaining higher-order folding (secondary/tertiary/quaternary), while the covalent peptide bonds of the primary sequence remain intact.",
    "Primary structure (the sequence itself) is not broken by typical denaturation (heat, pH change); molecular weight and amino acid composition remain the same after denaturation.",
    "Denaturation causes loss of biological activity (e.g., enzyme function) due to loss of specific 3D conformation, without breaking the peptide backbone.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-m-04","Medium","Which statement about enzyme active sites is correct?",
    ["The active site binds any substrate non-specifically","The active site is a specific region that binds substrate with high specificity, often described by the lock-and-key or induced-fit model","The active site is where ATP is always produced","Active sites are found only in RNA enzymes"],"B",
    "Enzyme active sites are specific 3D regions shaped to bind particular substrates, explained by the lock-and-key model (rigid fit) or the more accurate induced-fit model (dynamic conformational change upon binding).",
    "Active sites are highly specific, not non-specific; ATP production is not a universal enzyme active-site function; most enzymes are proteins, not RNA (though ribozymes exist as an exception).",
    "Enzyme specificity arises from the precise arrangement of amino acid side chains within the active site.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-m-05","Medium","Which of the following amino acids contains sulfur in its side chain?",
    ["Glycine","Cysteine","Alanine","Valine"],"B",
    "Cysteine contains a thiol (-SH) group in its side chain, providing the sulfur that allows disulfide bond formation between cysteine residues.",
    "Glycine, alanine, and valine have simple hydrocarbon-based side chains without sulfur.",
    "Disulfide bonds (S-S) formed between cysteine residues significantly stabilize protein tertiary and quaternary structure.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-m-06","Medium","Glycogen differs from starch mainly in that glycogen:",
    ["Is found only in plants","Is more highly branched than amylopectin","Is a monosaccharide","Lacks glucose units"],"B",
    "Glycogen has a more extensively branched structure than amylopectin (the branched component of starch), allowing rapid glucose mobilization in animals.",
    "Glycogen is the animal storage polysaccharide (not plant); it is a polysaccharide, not a monosaccharide; it is entirely composed of glucose units, like starch.",
    "Both starch and glycogen are glucose storage polymers, but glycogen's higher branching suits the faster metabolic demands of animals.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-m-07","Medium","Which of the following best explains why enzyme activity typically decreases sharply above the optimum temperature?",
    ["The enzyme runs out of substrate","High temperature denatures the enzyme's 3D structure, disrupting the active site","The enzyme becomes more specific","Reaction rate always increases indefinitely with temperature"],"B",
    "Beyond the optimum temperature, excess thermal energy disrupts the weak bonds maintaining enzyme conformation, denaturing the protein and destroying the functional shape of the active site.",
    "Substrate depletion is a separate kinetic factor unrelated to the temperature-denaturation relationship; enzymes don't become 'more specific' with heat; reaction rate does NOT increase indefinitely — it drops sharply post-optimum due to denaturation.",
    "Enzyme activity generally rises with temperature up to an optimum (increased kinetic energy/collisions), then falls sharply as denaturation sets in.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-m-08","Medium","Which bond connects the sugar and phosphate backbone in a nucleic acid strand?",
    ["Peptide bond","Glycosidic bond","Phosphodiester bond","Hydrogen bond"],"C",
    "Phosphodiester bonds link the 3' carbon of one sugar to the 5' phosphate of the next nucleotide, forming the sugar-phosphate backbone of DNA/RNA.",
    "Peptide bonds link amino acids in proteins; glycosidic bonds link the base to the sugar within a single nucleotide; hydrogen bonds hold complementary base pairs together between strands, not the backbone itself.",
    "The phosphodiester backbone is directional (5' to 3'), which underlies the antiparallel structure of double-stranded DNA.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-m-09","Medium","Competitive enzyme inhibitors work by:",
    ["Binding permanently to the enzyme, destroying it","Structurally resembling the substrate and competing for the active site","Binding only to the enzyme-substrate complex","Increasing the enzyme's affinity for substrate"],"B",
    "Competitive inhibitors have a structure similar to the natural substrate, allowing them to bind to the active site and block substrate binding, but this effect can be overcome by increasing substrate concentration.",
    "Competitive inhibition is typically reversible, not a permanent/destructive binding; binding to the enzyme-substrate complex describes uncompetitive inhibition; competitive inhibitors decrease, not increase, effective substrate binding.",
    "Because competitive inhibitors compete directly for the same site, their effect can be reduced by raising substrate concentration.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-m-10","Medium","Which of the following best describes the role of chaperone proteins?",
    ["They catalyze DNA replication","They assist in the proper folding of other proteins","They transport oxygen in blood","They form the cell membrane structure"],"B",
    "Chaperone proteins (e.g., heat shock proteins) assist nascent or stress-denatured polypeptides in folding correctly into their functional 3D conformation.",
    "DNA replication involves polymerases, not chaperones; oxygen transport is the role of hemoglobin; membrane structure primarily involves lipids and membrane proteins, not chaperones.",
    "Chaperones prevent misfolding and aggregation, which is critical since a protein's function depends on its correct 3D shape.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-m-11","Medium","Which statement about essential amino acids is correct?",
    ["They can be synthesized by the human body in sufficient quantity","They must be obtained through the diet since the body cannot synthesize them adequately","They are only found in plant proteins","They do not participate in protein synthesis"],"B",
    "Essential amino acids cannot be synthesized by the human body in adequate amounts and must be supplied through diet.",
    "It is non-essential amino acids that the body can synthesize sufficiently; essential amino acids are found in both plant and animal protein sources; they are standard amino acids fully involved in protein synthesis.",
    "There are 9 essential amino acids in humans; a complete protein source provides all of them in adequate proportions.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-m-12","Medium","Which of the following is true regarding quaternary protein structure?",
    ["It refers to a single polypeptide's amino acid sequence","It involves the assembly of two or more polypeptide subunits into a functional protein complex","It only occurs in enzymes","It is always identical to tertiary structure"],"B",
    "Quaternary structure describes how multiple folded polypeptide subunits associate to form a larger, functional multi-subunit protein complex.",
    "A single polypeptide's sequence describes primary structure; quaternary structure occurs in many protein types (not only enzymes, e.g., hemoglobin is a transport protein); it is distinct from tertiary structure, which refers to a single chain's 3D shape.",
    "Hemoglobin is a classic example: four polypeptide subunits (2 alpha + 2 beta) associate to form the functional protein.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-m-13","Medium","Which of the following correctly pairs a biomolecule with its monomer?",
    ["Protein — glucose","Nucleic acid — nucleotide","Starch — amino acid","Lipid — nucleotide"],"B",
    "Nucleic acids are correctly paired with nucleotides as their repeating monomer unit.",
    "Proteins are made of amino acids (not glucose); starch is made of glucose (not amino acids); lipids are not polymers of nucleotides — they're typically glycerol + fatty acids.",
    "Correct pairings: protein-amino acid, carbohydrate(polysaccharide)-monosaccharide, nucleic acid-nucleotide; lipids are generally not considered true polymers in the same sense.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-m-14","Medium","Which of the following best explains why enzymes increase reaction rates?",
    ["They increase the free energy of the reaction","They lower the activation energy required for the reaction to proceed","They change the equilibrium position of the reaction","They provide the substrate needed for the reaction"],"B",
    "Enzymes function as catalysts by lowering the activation energy barrier, allowing the reaction to proceed faster without altering the overall thermodynamics.",
    "Enzymes do not increase free energy; catalysts (including enzymes) do not shift equilibrium position, only the rate of reaching it; enzymes act on substrate but do not 'provide' it — substrate must already be present.",
    "By stabilizing the transition state, enzymes drastically speed up reactions that would otherwise occur too slowly to sustain life.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-m-15","Medium","Which pH condition would most likely denature a typical human digestive enzyme like pepsin's optimal environment if reversed?",
    ["Extremely acidic pH (like stomach pH ~2) for pepsin, which actually requires this acidic pH to function","Neutral pH for pepsin (since pepsin needs acidic pH, neutral pH would reduce its activity)","Any pH has no effect on pepsin","High temperature only affects pepsin, not pH"],"B",
    "Pepsin is specifically adapted to function optimally at the highly acidic pH of the stomach (~pH 2); shifting it to neutral pH would disrupt its ionizable side chain interactions and reduce/abolish activity.",
    "Acidic pH is pepsin's optimal condition, not a denaturing one; pH does affect enzyme activity/structure significantly; both pH and temperature independently affect enzyme structure, not just temperature.",
    "Each enzyme has a characteristic optimum pH reflecting its physiological environment — pepsin (stomach, acidic) versus trypsin (small intestine, mildly alkaline), for example.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

# ============ HARD (15) ============
add("bm-h-01","Hard","Which of the following best explains why a single amino acid substitution (e.g., in sickle cell hemoglobin) can drastically alter protein function?",
    ["All amino acid substitutions have identical effects on protein structure","A substitution can change the local chemical properties (e.g., polarity/charge), potentially disrupting folding, interactions, or function, depending on its location","Amino acid substitutions never affect tertiary structure","Substitutions only affect the protein's molecular weight"],"B",
    "In sickle cell disease, a single substitution (glutamic acid to valine) changes a charged, polar residue to a nonpolar one at a critical surface position, altering hemoglobin's solubility and causing it to polymerize into rigid fibers under low oxygen — drastically changing function despite being just one amino acid change.",
    "Substitution effects vary enormously depending on position and chemical nature — not identical for all cases; substitutions absolutely can affect tertiary structure via altered folding/interactions; molecular weight change from one substitution is functionally trivial compared to the actual structural/functional impact.",
    "This illustrates how the primary sequence critically determines higher-order structure and function — a cornerstone of protein biology (Anfinsen's principle).",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-h-02","Hard","In enzyme kinetics, what does a high Km value indicate about an enzyme's affinity for its substrate?",
    ["High affinity — the enzyme reaches half-maximal velocity at a low substrate concentration","Low affinity — a higher substrate concentration is needed to reach half-maximal velocity","Km has no relation to substrate affinity","High Km means the enzyme is always more efficient"],"B",
    "Km is the substrate concentration at which reaction velocity is half of Vmax; a HIGH Km means a large amount of substrate is needed to achieve this half-maximal rate, indicating LOWER binding affinity between enzyme and substrate.",
    "High affinity actually corresponds to a LOW Km (reaching half-max velocity easily, at low substrate); Km is fundamentally a measure related to (inversely correlated with) substrate affinity; high Km does not imply greater efficiency — it implies weaker binding, and efficiency is better reflected by kcat/Km.",
    "Michaelis-Menten kinetics: Km is inversely related to enzyme-substrate affinity — smaller Km = tighter binding/higher affinity.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-h-03","Hard","Why is the antiparallel orientation of the two DNA strands functionally significant?",
    ["It has no functional significance, it's purely structural coincidence","It allows complementary base pairing (A-T, G-C) to occur correctly given the chemical directionality (5' to 3') of each strand","It prevents any hydrogen bonding between strands","It causes DNA to be single-stranded under normal conditions"],"B",
    "Because each DNA strand has an inherent chemical directionality (5' phosphate end to 3' hydroxyl end), the two strands must run in opposite (antiparallel) directions for the bases to align properly and form stable Watson-Crick base pairs (A-T, G-C) via hydrogen bonding.",
    "This orientation is functionally essential, not coincidental; antiparallel strands specifically enable, not prevent, complementary hydrogen bonding; DNA is characteristically double-stranded under normal physiological conditions, not single-stranded.",
    "This antiparallel double helix structure (Watson-Crick model) is fundamental to accurate DNA replication and repair mechanisms.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-h-04","Hard","Which of the following best explains allosteric enzyme regulation?",
    ["A molecule binds directly to the active site, competing with substrate","A regulatory molecule binds at a site other than the active site, causing a conformational change that affects enzyme activity","Allosteric regulation only increases enzyme activity, never decreases it","Allosteric enzymes lack a defined active site"],"B",
    "Allosteric regulation involves an effector molecule binding to a distinct regulatory (allosteric) site, inducing a conformational shift in the enzyme that alters the shape/accessibility of the active site, thereby modulating (increasing or decreasing) activity.",
    "Direct active-site competition describes competitive inhibition, not allosteric regulation; allosteric effectors can be either activators (increase activity) or inhibitors (decrease activity) — not only one direction; allosteric enzymes do have a defined active site, plus the separate regulatory site.",
    "Allosteric regulation is a key mechanism for feedback inhibition in metabolic pathways, where the end product often allosterically inhibits an early pathway enzyme.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-h-05","Hard","Why does boiling an enzyme-containing solution typically result in irreversible loss of enzymatic activity, unlike mild pH changes which may be reversible?",
    ["Boiling only removes the substrate, not the enzyme","Boiling provides enough energy to break not just weak stabilizing bonds but can also disrupt structure so extensively that the polypeptide aggregates/precipitates, preventing refolding, unlike mild reversible pH-induced unfolding","Mild pH changes destroy the primary structure permanently","Boiling has no effect on protein structure"],"B",
    "High heat provides substantial energy that can extensively unfold the protein and often causes aggregation/precipitation of exposed hydrophobic regions, making the original conformation very difficult or impossible to restore — unlike a mild, reversible pH shift that may only partially disrupt weak interactions without causing aggregation.",
    "Boiling denatures the enzyme itself, not merely removing substrate; mild pH changes do NOT destroy primary (covalent peptide bond) structure — that's the whole point of reversibility; boiling very much affects protein structure through extensive denaturation.",
    "Reversibility of denaturation depends on the severity and nature of the disrupting condition — mild, transient changes are often reversible (renaturation), while extreme, aggregating conditions like boiling usually are not.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-h-06","Hard","Which best explains why RNA, despite being generally single-stranded, can still fold into complex secondary structures like hairpin loops?",
    ["RNA cannot fold at all","Complementary base sequences within the same single RNA strand can pair with each other, folding the molecule back on itself","RNA folding only occurs due to protein assistance","RNA lacks the ability to form hydrogen bonds"],"B",
    "Even though RNA is single-stranded overall, internal complementary sequences within that same strand can base-pair with each other (intramolecular pairing), causing the strand to fold back and form stem-loop (hairpin) structures.",
    "RNA absolutely can and does fold into complex 3D shapes; while some folding is protein-assisted, the fundamental capacity comes from its own sequence-based intramolecular pairing; RNA bases readily form hydrogen bonds (A-U, G-C), which is the basis of this folding.",
    "This self-pairing capacity underlies functional RNA structures like tRNA's cloverleaf shape and various catalytic/regulatory RNA structures.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-h-07","Hard","Why can a small change in solution pH significantly affect enzyme activity even without full denaturation?",
    ["pH changes always fully denature the enzyme immediately","pH affects the ionization state of amino acid side chains at/near the active site, which can alter substrate binding and catalytic efficiency without necessarily causing complete unfolding","pH has no effect on amino acid side chains","Enzymes are entirely unaffected by their chemical environment"],"B",
    "Amino acid side chains (like the carboxyl or amino groups of certain residues) have specific ionization states that depend on pH; shifts in pH can alter these charges at or near the active site, affecting substrate binding or the catalytic mechanism, even before the protein's overall fold is disrupted.",
    "A small pH change does not necessarily cause full/immediate denaturation — the effects can be more subtle initially; pH absolutely influences side chain ionization (that's basic amino acid chemistry); enzymes are highly sensitive to their chemical environment, including pH.",
    "This explains why enzymes have characteristic pH optima — deviations reduce activity progressively before potentially causing full denaturation at more extreme pH.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-h-08","Hard","Which best explains the biological significance of the fact that most biomolecules in living systems are chiral (exist in specific stereoisomeric forms, e.g., L-amino acids, D-sugars)?",
    ["Chirality has no functional significance in biology","Enzymes and biological receptors are themselves chiral structures, so they interact stereospecifically — using the 'wrong' stereoisomer would prevent proper binding/function","All stereoisomers behave identically in biological systems","Chirality only matters for carbohydrates, not proteins or nucleic acids"],"B",
    "Since enzymes and receptors are built from chiral molecules (like L-amino acids) with a specific 3D shape, they can typically only recognize and properly bind one specific stereoisomer of a substrate — this stereospecificity means that using the 'wrong' mirror-image form of a molecule often results in no interaction or a completely different (sometimes harmful) effect.",
    "Chirality has major functional significance in biology (it's not irrelevant); stereoisomers frequently show drastically different biological behavior (e.g., different smell/taste, or drug efficacy vs toxicity); chirality is relevant across all major biomolecule classes — proteins (L-amino acids), carbohydrates (D-sugars), and nucleic acids (specific sugar configurations), not just carbohydrates.",
    "This principle explains why pharmaceutical companies must carefully control stereochemistry in drug synthesis, since one enantiomer may be therapeutic while its mirror image is inactive or toxic.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-h-09","Hard","Why is cellulose largely indigestible to humans while starch is readily digestible, despite both being glucose polymers?",
    ["Cellulose contains a different sugar than starch","Cellulose's beta-1,4-glycosidic bonds cannot be broken by human digestive enzymes (which are specific for starch's alpha-1,4 bonds), while herbivores/ruminants rely on symbiotic microbes with cellulase enzymes","Starch and cellulose have identical bonding, but humans simply choose not to digest cellulose","Cellulose is toxic to human digestive enzymes"],"B",
    "Cellulose and starch are both glucose polymers, but they differ in the type of glycosidic linkage: cellulose has beta-1,4 bonds, while starch has alpha-1,4 bonds. Human digestive enzymes (amylases) are specific for the alpha linkage and cannot hydrolyze the beta linkage, so cellulose passes through mostly undigested (as dietary fiber) — while herbivores use symbiotic gut microbes producing cellulase to break it down.",
    "Both are made purely of glucose (same monomer); the difference is bond geometry, not sugar identity; it is not a matter of 'choice' but of enzyme specificity — human amylase structurally cannot act on beta linkages; cellulose isn't toxic to enzymes, simply not a substrate for them.",
    "This alpha vs beta linkage distinction is a classic example of how a small structural difference (glycosidic bond stereochemistry) leads to vastly different digestibility and function despite identical monomer composition.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-h-10","Hard","Which best describes why phosphate groups are critical to nucleic acid structure and function beyond just forming the backbone?",
    ["Phosphate groups have no function beyond structural backbone linkage","The negatively charged phosphate groups contribute to DNA/RNA's overall negative charge, influencing interactions with positively charged proteins (like histones) and affecting molecular packaging and interactions","Phosphate groups are only present in RNA, not DNA","Phosphate groups prevent any protein from binding to DNA"],"B",
    "Beyond linking nucleotides via phosphodiester bonds, the phosphate groups give DNA/RNA a strong overall negative charge, which is essential for interactions with positively charged proteins like histones (enabling DNA packaging into chromatin) and influences many DNA-protein interactions in general.",
    "Phosphate groups have significant additional functional roles beyond mere backbone linkage; phosphate groups are present in both DNA and RNA equally, not RNA-exclusive; far from preventing protein binding, the phosphate charge actually facilitates specific and non-specific interactions with many DNA-binding proteins.",
    "This negative charge is also exploited experimentally, e.g., in gel electrophoresis, where DNA migrates toward the positive electrode due to its phosphate-based negative charge.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-h-11","Hard","Why might a mutation affecting a cysteine residue involved in a disulfide bond have a more significant structural impact than a mutation affecting a residue only involved in hydrogen bonding?",
    ["Disulfide bonds are always weaker than hydrogen bonds","Disulfide (covalent) bonds are generally stronger and more critical for locking specific tertiary/quaternary structural elements in place compared to individual, more easily reformed hydrogen bonds","Cysteine residues have no structural role","Hydrogen bonds are always more important than disulfide bonds"],"B",
    "Disulfide bonds are covalent (much stronger than the weak, individually reversible hydrogen bonds) and often lock together distant parts of a folded protein or separate subunits; losing a disulfide bond (e.g., via cysteine mutation) can therefore cause more drastic destabilization than losing a single hydrogen bond, which is one of many similar weak interactions that can partially compensate for each other.",
    "Disulfide bonds are actually stronger (covalent) than individual hydrogen bonds (weak, non-covalent), not weaker; cysteine residues are structurally significant precisely because of their disulfide-forming capacity; the relative importance depends on context, but covalent disulfide bonds are generally more structurally 'locking' than a single hydrogen bond.",
    "This is why disulfide-rich proteins (like antibodies, keratin) tend to be especially stable and resistant to denaturation compared to proteins relying mainly on hydrogen bonding.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-h-12","Hard","In feedback inhibition of a metabolic pathway, why is it advantageous for the end product to inhibit an early enzyme in the pathway rather than the last enzyme?",
    ["Inhibiting the last enzyme would be equally efficient in every way","Inhibiting an early enzyme prevents the cell from wasting energy and resources synthesizing all the intermediate compounds that would otherwise accumulate uselessly if only the final step were blocked","Feedback inhibition always targets the last enzyme, never an early one","There is no advantage; enzyme position in the pathway is irrelevant"],"B",
    "By inhibiting an early, often rate-limiting enzyme, the cell prevents the formation of all downstream intermediates once the end product is in sufficient supply — conserving energy and raw materials that would otherwise be wasted producing intermediates that lead to a blocked final step.",
    "Inhibiting only the last enzyme would still allow all upstream intermediates to accumulate wastefully, which is inefficient compared to early inhibition; feedback inhibition characteristically targets an early, often committed/rate-limiting step, not exclusively the last enzyme; enzyme position very much matters for pathway efficiency.",
    "This regulatory logic (end-product inhibition of an early, committed step) is a recurring theme in metabolic pathway regulation across biology.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-h-13","Hard","Why do globular proteins (like enzymes) typically have hydrophobic amino acids clustered in their interior and hydrophilic amino acids on their surface when folded in an aqueous environment?",
    ["This arrangement is random and has no functional basis","Hydrophobic residues avoid contact with water by clustering internally (driven by the hydrophobic effect), while hydrophilic residues remain surface-exposed to interact favorably with the surrounding aqueous environment, stabilizing the folded structure","Hydrophilic residues are always toxic if exposed to water","All amino acids have identical water affinity, so no such pattern exists"],"B",
    "In an aqueous cellular environment, nonpolar (hydrophobic) side chains minimize unfavorable interactions with water by burying themselves in the protein's interior, driven by the hydrophobic effect; polar/charged (hydrophilic) side chains remain on the exterior, forming favorable hydrogen bonds and electrostatic interactions with surrounding water — this arrangement is thermodynamically stable and central to proper protein folding.",
    "This pattern is not random — it's a fundamental, energetically driven principle of protein folding; hydrophilic residues are not toxic when exposed to water, quite the opposite, they are stabilized by it; amino acids have markedly different water affinities based on their side chain chemistry (this variation is the whole basis of the folding principle).",
    "This hydrophobic-core/hydrophilic-surface arrangement is a major driving force in tertiary structure formation and protein stability in aqueous solution.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-h-14","Hard","Which best explains why the genetic code stored in DNA must first be transcribed into RNA before translation into protein, rather than being translated directly from DNA?",
    ["DNA cannot leave the nucleus and ribosomes (in eukaryotes) are in the cytoplasm, so RNA acts as a mobile intermediate carrying the genetic message; also, using RNA as an intermediate protects the original DNA template from repeated handling/damage during translation","There is no functional reason; it is an arbitrary biological process","DNA is directly translated in all organisms without transcription","RNA is not actually involved in protein synthesis"],"A",
    "In eukaryotic cells, DNA remains confined to the nucleus, while ribosomes (protein synthesis machinery) are located in the cytoplasm — RNA (mRNA) serves as a mobile, disposable copy of the genetic information that can be exported to the cytoplasm for translation, while also protecting the original DNA from the wear of repeated direct use.",
    "There is a clear evolutionary and functional logic (compartmentalization, protection of the genetic template) rather than arbitrariness; DNA is not directly translated in normal cellular protein synthesis — transcription to RNA is a universal intermediate step; RNA (specifically mRNA, along with tRNA and rRNA) is absolutely central to protein synthesis.",
    "This central dogma flow (DNA → RNA → protein) reflects both the physical compartmentalization in eukaryotic cells and an efficient division of labor between information storage (DNA) and information use (RNA).",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

add("bm-h-15","Hard","Why can two proteins with very different amino acid sequences sometimes have very similar overall tertiary structures and functions (structural convergence)?",
    ["This never actually happens in biology","Different sequences can still fold into similar overall 3D shapes if the pattern of hydrophobic/hydrophilic residues and key structural motifs are functionally equivalent, since tertiary structure depends more on the general chemical pattern than the exact sequence identity at every position","All proteins with different sequences always have completely different structures","Protein structure is entirely independent of amino acid sequence"],"B",
    "Tertiary structure formation depends heavily on the overall pattern of hydrophobic/hydrophilic distribution and the presence of key stabilizing interactions (like specific structural motifs), rather than requiring an identical sequence at every single position — so different sequences can still converge on similar folds if they preserve these essential structural/chemical patterns.",
    "Structural convergence with different sequences is a well-documented phenomenon in protein biology, not a myth; while different sequences CAN also lead to completely different structures, they don't always have to — convergence is real; protein structure is fundamentally dependent on sequence (Anfinsen's principle), just not necessarily on exact identity at every residue.",
    "This concept underlies 'convergent evolution' at the molecular level, where unrelated protein families independently evolve similar functional folds.",
    "NCERT Class 11 Biology, Ch. 9 Biomolecules")

with open('/mnt/user-data/outputs/biomolecules.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(questions)} questions")
print("Easy:", sum(1 for q in questions if q['difficulty']=='Easy'))
print("Medium:", sum(1 for q in questions if q['difficulty']=='Medium'))
print("Hard:", sum(1 for q in questions if q['difficulty']=='Hard'))
