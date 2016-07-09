package YelpCategoryPrediction.QueryGeneratorModule;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;

import org.apache.lucene.document.Document;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.Term;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TermQuery;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.FSDirectory;
import YelpCategoryPrediction.Constants.*;

/**
 * @author Renuka
 * Class to build queries for each category
 */
public class QueryOptimizer {

	public static IndexReader reader = null;
	public static IndexSearcher searcher = null;
	FileAccess fa = null;
	
	/**
	 * Initialize lucene reader and searcher
	 */
	public void initIndex() {

		try {
			reader = DirectoryReader
					.open(FSDirectory.open(Paths
							.get(Constants.trainIndex)));
			searcher = new IndexSearcher(reader);
			fa = new FileAccess();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	
	/**
	 * Function to build queries for each category
	 * @param categories - categories to build queries for
	 */
	public void buildQueries(ArrayList<String> categories) {

		try {

			
			for (String category : categories) {
				//1. Read a category from arraylist
				category = category.trim();
				//2. get all documents for this category from train index
				TopDocs topdocs = getDocsForCategory(category);
				//3. get a consolidated string of reviews and tips for all docs obtained in step 2
				String text = getConsolidatedReviewAndTipForCategory(topdocs);
				//4. save this consolidated string in a file
				saveTextToFile(text);
				//5. extract nouns from this text using stanford pos-tagger library
				ArrayList<String> nouns = getNounsForCategory(text);
				//6. get top n words from these nouns with highest TFIDF score in category  
				ScoreCalculator sc = new ScoreCalculator();
				ArrayList<String> top100 = sc.getTopQueryWordsForCategory(nouns, topdocs, category);
				//7. write these top n nouns in file
				writeQueryToFile(category + " : " + top100.toString());
			}
			System.out.println();

		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	
	/**
	 * Function to write text to a temporay file
	 * @param text
	 */
	public void saveTextToFile(String text){
		text.replaceAll(".", " ");
		fa.WriteToFile(fa.getWorkingFile(), text);
	}
	
	/**
	 * Function to extract nouns from review and tip string
	 * @param text
	 * @return - arraylist of all nouns present in text
	 */
	public ArrayList<String> getNounsForCategory(String text){
		Tagger tag = new Tagger();
		ArrayList<String> nouns = tag.tagText(fa.getWorkingFile());
		return nouns;
	}

	
	/**
	 * Function to get all documents for category from lucene train index
	 * @param category
	 * @return TopDocs for given category
	 */
	public TopDocs getDocsForCategory(String category) {
		TermQuery qry = new TermQuery(new Term("categories", category));
		TopDocs topdocs = null;
		try {
			topdocs = searcher.search(qry, Integer.MAX_VALUE);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return topdocs;
	}

	/**
	 * Function to consolidate all review and tips for a category into one string
	 * @param topdocs
	 * @return - consolidated string for review and tips
	 */
	public String getConsolidatedReviewAndTipForCategory(TopDocs topdocs) {
		String text = "";
		try {
			for (ScoreDoc sdoc : topdocs.scoreDocs) {
				Document doc;

				doc = reader.document(sdoc.doc);

				String reviewAndTip = doc.get("reviewsandtips");
				text = text.concat(reviewAndTip);
				text = text.concat(" ");

			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return text;
	}

	/**
	 * Function to final query to the query file
	 * @param text
	 */
	public void writeQueryToFile(String query){
		
		fa.AppendAtEnd(fa.getQueryFile(), query);
		fa.AppendAtEnd(fa.getQueryFile(), "\n\n");
	}
}
