package YelpCategoryPrediction.QueryGeneratorModule;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

import YelpCategoryPrediction.Constants.Constants;
import edu.stanford.nlp.ling.Sentence;
import edu.stanford.nlp.ling.TaggedWord;
import edu.stanford.nlp.ling.HasWord;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.process.CoreLabelTokenFactory;
import edu.stanford.nlp.process.DocumentPreprocessor;
import edu.stanford.nlp.process.PTBTokenizer;
import edu.stanford.nlp.process.TokenizerFactory;
import edu.stanford.nlp.tagger.maxent.MaxentTagger;

/**
 * @author Renuka Class for POS tagging text and extracting nouns
 */
public class Tagger {

	public Tagger() {
	}

	/**
	 * Function to parse text using the left-3-words tagger model and extracting
	 * nouns
	 * 
	 * @param text
	 * @return - list of nouns from text
	 */
	/**
	 * @param text
	 * @return
	 */
	public ArrayList<String> tagText(String text) {

		ArrayList<String> nouns = new ArrayList<String>();
		try {

			MaxentTagger tagger = new MaxentTagger(Constants.taggermodel);

			TokenizerFactory<CoreLabel> ptbTokenizerFactory = PTBTokenizer
					.factory(new CoreLabelTokenFactory(),
							"untokenizable=noneKeep");
			BufferedReader r = new BufferedReader(new InputStreamReader(
					new FileInputStream(text), "utf-8"));
			PrintWriter pw = new PrintWriter(new OutputStreamWriter(System.out,
					"utf-8"));
			DocumentPreprocessor documentPreprocessor = new DocumentPreprocessor(
					r);

			// tag text
			documentPreprocessor.setTokenizerFactory(ptbTokenizerFactory);
			for (List<HasWord> sentence : documentPreprocessor) {
				List<TaggedWord> tSentence = tagger.tagSentence(sentence);
				// extract nouns
				for (TaggedWord tw : tSentence) {
					if (tw.tag().startsWith("NN")) {
						nouns.add(tw.word());
					}
				}
			}

			pw.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return nouns;
	}

}
