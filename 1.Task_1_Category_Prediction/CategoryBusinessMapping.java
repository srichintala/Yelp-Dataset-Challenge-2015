package YelpCategoryPrediction.QueryConsumerModule;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;

import org.apache.lucene.document.Document;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.Term;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TermQuery;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.FSDirectory;

import YelpCategoryPrediction.QueryGeneratorModule.FileAccess;
import YelpCategoryPrediction.QueryGeneratorModule.ScoreCalculator;
import YelpCategoryPrediction.Constants.*;

/**
 * @author Renuka
 * Class to generate ground truth file on test index for evaluation purposes 
 */
public class CategoryBusinessMapping {
	public static IndexReader reader = null;
	public static IndexSearcher searcher = null;
	public static ArrayList<String> categories;

	public static String groundTruthFile = Constants.groundTruthFile;

	/**
	 * Function to initialize lucene reader and searcher
	 */
	public void initIndex() {

		try {
			reader = DirectoryReader
					.open(FSDirectory.open(Paths
							.get(Constants.testIndex)));
			searcher = new IndexSearcher(reader);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	/**
	 * Function to read category names from categories file
	 */
	public void setCategories() {
		FileAccess fa = new FileAccess();
		categories = fa.ReadFromFile(fa.getIndexFile());
		;
	}

	/**
	 * Function to build the ground truth file from lucene test index
	 */
	public void buildGroundTruthFile() {
		try {

			for (String category : categories) {
				System.out.println(category);
				category = category.trim();
				
				//get topdocs for category
				TopDocs topdocs = getDocsForCategory(category);

				ArrayList<String> bussIds = new ArrayList<String>();
				
				//for each document in scoredocs, extract the business id and add to list
				for (ScoreDoc scoreDoc : topdocs.scoreDocs) {
					Document doc = reader.document(scoreDoc.doc);
					String businessId = doc.get("business_id");
					bussIds.add(businessId);

				}
				//save output to file
				writeQueryToFile(category + " : " + bussIds.toString());
			}
			System.out.println();

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * function to get documents with the given category
	 * @param category - category to get documents for
	 * @return - all documents having the category
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
	 * Function to write output to file
	 * @param query
	 */
	public void writeQueryToFile(String query) {

		FileAccess fa = new FileAccess();
		fa.AppendAtEnd(groundTruthFile, query);
		fa.AppendAtEnd(groundTruthFile, "\n");
	}

	public static void main(String[] args) {
		CategoryBusinessMapping cbm = new CategoryBusinessMapping();
		cbm.initIndex();
		cbm.setCategories();
		cbm.buildGroundTruthFile();
		System.out.println("DONE!!");

	}

}
