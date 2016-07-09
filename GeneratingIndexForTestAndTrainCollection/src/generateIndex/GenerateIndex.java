package generateIndex;

import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.util.BytesRef;
import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Field;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field.Store;
import org.apache.lucene.document.StringField;
import org.apache.lucene.document.TextField;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig; 

import com.mongodb.BasicDBObject;
import com.mongodb.BasicDBObjectBuilder;
import com.mongodb.Bytes;
import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.DBCursor;
import com.mongodb.DBObject;
import com.mongodb.Mongo;
import com.mongodb.MongoClient;
import com.mongodb.MongoException;
import com.mongodb.util.JSON;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import org.json.simple.parser.ParseException;

/*
 * Creates training and test indexes using lucene
 * For each record in the training and test collections in mongodb,
 * gets the business_id, categories, combines reviews and tips,
 * then adds it to the lucene document.
 */
public class GenerateIndex {
	public static void main(String[] args) throws IOException, ParseException 
	{ 
		MongoClient mongoClient = new MongoClient( "localhost" , 27017 );
		DB db = mongoClient.getDB( "yelp" );
						
		Directory trainingIndexPath = FSDirectory.open(Paths.get("K:\\IUB Sem-3\\Search- Information Retrieval-Z534\\Project\\trainingIndex"));
		Directory testIndexPath = FSDirectory.open(Paths.get("K:\\IUB Sem-3\\Search- Information Retrieval-Z534\\Project\\testIndex"));
			
		generateTrainingIndex(trainingIndexPath, db);
		generateTestIndex(testIndexPath, db);
		IndexReader trainingReader = DirectoryReader.open(trainingIndexPath);
        int trainingDocs = trainingReader.maxDoc();
        System.out.println("The total docs in training index file are:" +trainingDocs);
        IndexReader testReader = DirectoryReader.open(testIndexPath);
        int testDocs = testReader.maxDoc();
        System.out.println("The total docs in test index file are:" +testDocs);
	}

	private static void generateTrainingIndex(Directory trainingIndexPath, DB db) throws IOException {
		// TODO Auto-generated method stub
		
		Analyzer Analyzer = new StandardAnalyzer();
        IndexWriterConfig iwc = new IndexWriterConfig(Analyzer);
        iwc.setOpenMode(IndexWriterConfig.OpenMode.CREATE);
        IndexWriter trainingWriter = new IndexWriter(trainingIndexPath, iwc);
        DBCollection trainingColl = db.getCollection("trainingData");
        DBObject query = new BasicDBObject();
        query.put("_id", 0);
        DBCursor trainingDataCursor = trainingColl.find(new BasicDBObject(), query).addOption(Bytes.QUERYOPTION_NOTIMEOUT);

        DBObject object;
        String business_ID = "";
        List <String> reviewText;
		List <String> tipText;
		List <String> categories;
		
		while(trainingDataCursor.hasNext())
		{
			object = trainingDataCursor.next();

			Document trainingDoc = new Document();
			business_ID = object.get("business_id").toString();
			trainingDoc.add(new StringField("business_id", business_ID, Store.YES));
	        String reviewsPlusTips = "";
			categories= (List <String>)object.get("categories");
			for(Object category : categories)
			{
				trainingDoc.add(new StringField("categories", category.toString(), Store.YES));
				System.out.println("categories: " +category.toString());
			}

			reviewText=(List<String>)object.get("review");
			for (Object review : reviewText)
			{
				reviewsPlusTips+=review.toString();
				System.out.println("REVIEWS: " +review);
			}
			tipText=(List<String>)object.get("tip");
			for (Object tip : tipText)
			{
				reviewsPlusTips+=tip.toString();
				System.out.println("TIPS : " +tip);
			}
			
			trainingDoc.add(new TextField("reviewsandtips", reviewsPlusTips, Store.YES));
			trainingWriter.addDocument(trainingDoc);
		}
		indexingDone(trainingDataCursor, trainingWriter);
	}

	private static void generateTestIndex(Directory testIndexPath, DB db) throws IOException {
		// TODO Auto-generated method stub
		Analyzer Analyzer = new StandardAnalyzer();
        IndexWriterConfig iwc = new IndexWriterConfig(Analyzer);
        iwc.setOpenMode(IndexWriterConfig.OpenMode.CREATE);
		IndexWriter testWriter = new IndexWriter(testIndexPath, iwc);
		
		DBCollection testColl = db.getCollection("testData");
        DBObject query = new BasicDBObject();
        query.put("_id", 0);
        DBCursor testDataCursor = testColl.find(new BasicDBObject(), query).addOption(Bytes.QUERYOPTION_NOTIMEOUT);

        DBObject object;
        String business_ID = "";
        List <String> reviewText;
		List <String> tipText;
		List <String> categories;
		
		while(testDataCursor.hasNext())
		{
			object = testDataCursor.next();
			Document testDoc = new Document();
			business_ID = object.get("business_id").toString();
			testDoc.add(new StringField("business_id", business_ID, Store.YES));

	        String reviewsPlusTips = "";
			categories= (List <String>)object.get("categories");
			for(Object category : categories)
			{
				testDoc.add(new StringField("categories", category.toString(), Store.YES));
				System.out.println("categories: " +category.toString());
			}

			reviewText=(List<String>)object.get("review");
			for (Object review : reviewText)
			{
				reviewsPlusTips+=review.toString();
				System.out.println("REVIEWS: " +review);
			}
			tipText=(List<String>)object.get("tip");
			for (Object tip : tipText)
			{
				reviewsPlusTips+=tip.toString();
				System.out.println("TIPS : " +tip);
			}
			
			testDoc.add(new TextField("reviewsandtips", reviewsPlusTips, Store.YES));
			testWriter.addDocument(testDoc);
		}
		indexingDone(testDataCursor, testWriter);
	}

	private static void indexingDone(DBCursor Cursor,
			IndexWriter Writer) throws IOException {
		// TODO Auto-generated method stub
			Cursor.close();
			Writer.forceMerge(1);
			Writer.commit();
			Writer.close();
	}
}
