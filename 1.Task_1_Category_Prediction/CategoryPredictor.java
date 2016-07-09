package YelpCategoryPrediction.QueryConsumerModule;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map.Entry;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.LeafReaderContext;
import org.apache.lucene.queryparser.classic.ParseException;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.search.similarities.BM25Similarity;
import org.apache.lucene.search.similarities.DefaultSimilarity;
import org.apache.lucene.search.similarities.LMDirichletSimilarity;
import org.apache.lucene.search.similarities.LMJelinekMercerSimilarity;
import org.apache.lucene.store.FSDirectory;

import YelpCategoryPrediction.Constants.Constants;
import YelpCategoryPrediction.QueryGeneratorModule.FileAccess;

/**
 * @author Renuka
 * class to predict categories of business from the test dataset
 */
public class CategoryPredictor {

	/**
	 * Initialize lucene reader, searcher and other variables
	 */
	public CategoryPredictor() {
		try {
			reader = DirectoryReader.open(FSDirectory.open(Paths
					.get(Constants.testIndex)));
			searcher = new IndexSearcher(reader);
			outputFile = Constants.outputFile;
			categoryMap = new HashMap<String, Integer>();

			fa = new FileAccess();
			fa.deleteFile(outputFile);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private IndexReader reader = null;
	private IndexSearcher searcher = null;
	private FileAccess fa = null;
	private HashMap<String, Integer> categoryMap = null;

	private String outputFile;

	/**
	 * Function to read queries from the query file generated in the earlier module
	 * @return
	 */
	public ArrayList<String> getQueries() {
		ArrayList<String> queries = new ArrayList<String>();

		FileAccess fa = new FileAccess();
		queries = fa.ReadFromFile(fa.getQueryFile());
		return queries;
	}

	
	public void rankDocsForQuery(ArrayList<String> queries) {

		rank(queries, "lmj");
	}

	/**
	 * Function to rank documents for query using the algorithm input as paramater 
	 * @param queries - queries as read from the query file
	 * @param algo - algorithm to use for ranking
	 */
	public void rank(ArrayList<String> queries, String algo) {
		try {
			Analyzer analyzer = new StandardAnalyzer();
			for (String string : queries) {
				if (string.equals(""))
					continue;

				switch (algo) {
				case "bm25":
					searcher.setSimilarity(new BM25Similarity());
					break;

				case "vsm":
					searcher.setSimilarity(new DefaultSimilarity());
					break;

				case "lmd":
					searcher.setSimilarity(new LMDirichletSimilarity());
					break;

				case "lmj":
					searcher.setSimilarity(new LMJelinekMercerSimilarity(
							(float) 0.7));
					break;

				default:
					break;
				}
				String[] strs = string.split(":");
				String cat = strs[0].trim();
				System.out.println(cat);
				if (!categoryMap.containsKey(cat))
					categoryMap.put(cat, categoryMap.keySet().size() + 1);
				QueryParser parser = new QueryParser("reviewsandtips", analyzer);
				Query query;

				query = parser.parse(parser.escape(strs[1].trim()));

				TopDocs results = searcher.search(query, Integer.MAX_VALUE);

				saveScore(results.scoreDocs, cat);

			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}
	
	
	/**
	 * Function to extract top 75 business ids for each category and save the output to file
	 * @param docs
	 * @param category
	 */
	public void saveScore(ScoreDoc[] docs, String category) {

		int len = Math.min(75, docs.length);
		ArrayList<String> bussIds = new ArrayList<String>();
		try {
			//extract business id for doc and add to list
			for (ScoreDoc scoreDoc : docs) {
				Document doc = reader.document(scoreDoc.doc);
				String businessId = doc.get("business_id");
				bussIds.add(businessId);
				len--;
				if (len <= 0)
					break;

			}
			writeQueryToFile(category + " : " + bussIds.toString());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * Function to write output to file
	 * @param catMap
	 */
	public void writeQueryToFile(String catMap) {

		FileAccess fa = new FileAccess();
		fa.AppendAtEnd(outputFile, catMap);
		fa.AppendAtEnd(outputFile, "\n");
	}

}
