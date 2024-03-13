const { PubSub } = require('@google-cloud/pubsub');

// Create a Pub/Sub client
const projectId = 'syscourse-474'
const keyFilename = '../../syscourse-474-privatekey.json';

const pubsub = new PubSub({ projectId, keyFilename });

// Define the subscription name and topic name
const subscriptionName = 'new-product-sub';
const topicName = 'new-product';

// Get a reference to the subscription
const subscription = pubsub.subscription(subscriptionName);

// Subscribe to the topic
subscription.on('message', (message) => {
  // Handle the message here
  console.log(`Received message: ${message.id}`);
  console.log(`Data: ${message.data}`);
  
  // Acknowledge the message
  message.ack();
});

console.log(`Subscribed to topic ${topicName}`);
