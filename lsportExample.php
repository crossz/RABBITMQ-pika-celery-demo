<?php
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;

$connection = new AMQPStreamConnection(
    'prematch-rmq.lsports.eu',// Change to host of Prematch or InPlay
    5672,
    "MyEmail", // Change to your user name
    'Passw0rd1234',// Change to your password
    "Customers",
    false,
    'AMQPLAIN', //LOGIN MECHANISM, no need to change
    null,
    'en_US',
    1160, // timeout 1, no need to change
    1160, // timeout 2, no need to change
    null,
    false,
    580); // heartbeat, no need to change


/**
 * Channel Creation From Connection
 */

$channel = $connection->channel();
/**
 *  Your queue number as received from LSPORT (WITH _)
 */
$queue = "_102030_"; // package_id for Prematch or InPlay

/**
 * Message Consume
 * $msg->body is a buffer array , use toString to get it as JSON/XML
 */
$callback = function($msg) {
    echo "Event Received ", $msg->body, "\n";
};

$channel->basic_qos(0,1000,false);
$channel->basic_consume($queue, 'consumer', false, true,false,false,$callback);



/**
 * Endless while loop waiting for next message to arrive
 */
while(count($channel->callbacks)) {
    $channel->wait();
}