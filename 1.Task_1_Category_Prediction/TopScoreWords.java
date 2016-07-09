package YelpCategoryPrediction.QueryGeneratorModule;

import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;

import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.FSDirectory;

/**
 * @author Renuka
 * Sample program to get top words got "Thai" category
 * This sample code was only used to generate the word cloud for Thai category 
 */
public class TopScoreWords {

	
	public static void main(String[] args) {

		try {
			String category = "Thai";
			
			QueryOptimizer qo = new QueryOptimizer();
			qo.initIndex();
			//get topdocs for Thai category
			TopDocs topdocs = qo.getDocsForCategory(category);
			//build a consolidated string for tips and reviews
			String text = qo.getConsolidatedReviewAndTipForCategory(topdocs);
			qo.saveTextToFile(text);
			//get nouns from this string using standforf pos tagger
			ArrayList<String> nouns = qo.getNounsForCategory(text);
			
			//calculate top noun words for thai category
			ScoreCalculator sc = new ScoreCalculator();
			HashMap<String, Double> scores = sc.getTopQueryWordsForCategoryWithScore(nouns, topdocs, category);
			//save the output into a file. this output is then fed into R to build the word cloud
			FileAccess fa = new FileAccess();
			String file = "G://GitHub//Z534_InformationSearch//src//YelpCategoryPrediction//InputFiles//ThaiWordScore.txt";
			fa.deleteFile(file);
			fa.WriteToFile(file ,scores.toString() );
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}
