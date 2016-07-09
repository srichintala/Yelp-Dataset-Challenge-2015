package task1;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.json.simple.parser.ParseException;

import com.mongodb.BasicDBObject;
import com.mongodb.Bytes;
import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.DBCursor;
import com.mongodb.DBObject;
import com.mongodb.MongoClient;

/*
 * First the json files of business, review and tip 
 * are imported into mongodb through mongo shell.
 * Create test and train collections in mongodb.
 * For each business id, gets the categories, reviews and tips.
 * The loop is run for 60% of the business records and adds it to training collection.
 * The rest 40% is added to test collection.
 */
public class CreateTrainingAndTestCollections {

	public static void main(String[] args) throws IOException, ParseException 
	{
		MongoClient mongoClient = new MongoClient( "localhost" , 27017 );
		DB db = mongoClient.getDB( "yelp" );

		DBCollection businessCollection = db.getCollection( "businessData" );
		DBCollection reviewCollection = db.getCollection( "reviewData" );
		DBCollection tipsCollection = db.getCollection( "tipData" );	
		DBCollection trainingData = db.getCollection( "trainingData" );
		DBCollection testData = db.getCollection( "testData" );
		DBObject businessQuery;
		DBObject reviewQuery;
		DBObject tipQuery;
		DBObject businessObj;
		DBObject reviewObj;
		DBObject tipObj;
        DBCursor businessCursor;
        DBCursor reviewsCursor;
        DBCursor tipsCursor;
        int businessDocsCount = 0;
        String businessID = "";
        
        businessQuery = new BasicDBObject();
        businessQuery.put("_id", 0);
        businessQuery.put("business_id", 1);
        businessQuery.put("categories", 1);
        businessCursor = businessCollection.find(new BasicDBObject(), businessQuery).addOption(Bytes.QUERYOPTION_NOTIMEOUT);
			
        while (businessCursor.hasNext()) { 
        	businessObj = businessCursor.next();
        	System.out.println("business obj:  " +businessObj);
        	DBObject newDocument = new BasicDBObject(businessObj.toMap());
        	businessID=(String)businessObj.get("business_id");
        	List <String> reviewText = new ArrayList<String>();
        	List <Integer> reviewRating = new ArrayList<Integer>();
        	reviewQuery = new BasicDBObject("business_id", businessID);
			reviewsCursor=reviewCollection.find(reviewQuery);
        	//iterating over reviews to get the text and ratings 
			while (reviewsCursor.hasNext())
			{
				reviewObj=reviewsCursor.next();
				//System.out.println("review obj:  " +reviewObj);
				reviewText.add((String) reviewObj.get("text"));
				if (reviewObj.get("stars")!= null) {
					reviewRating.add((int)reviewObj.get("stars"));
				} else {
					reviewRating.add(0);					
				}
			}
			//adding the review data to the document 
			newDocument.put("review", reviewText);
			newDocument.put("reviewrating", reviewRating);
			
			//iterating over tip to get the text 
			tipQuery = new BasicDBObject("business_id",(String)businessObj.get("business_id"));
			tipsCursor=tipsCollection.find(tipQuery);
			List <String> tipText = new ArrayList<String>();
			while (tipsCursor.hasNext())
			{
				tipObj=tipsCursor.next();	
				//System.out.println("tip obj:  " +tipObj);
				tipText.add((String) tipObj.get("text"));				
			}
			//adding the tip data to the document 
			newDocument.put("tip", tipText);

			if(businessDocsCount <= 40382)
			{
				trainingData.insert(newDocument);
				businessDocsCount++;				
			}
			else
			{
				testData.insert(newDocument);
				businessDocsCount++;
			}
			
        }
		
	}

}
