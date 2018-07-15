# Submit a web form to an AWS API Gateway Endpoint and Lambda

Its very common to need to process some data for your website, such as a comment or
registration form. However modest server-side processing requirements like this shouldn't
require you to use a full blown CMS like Wordpress or Drupal.

This example will walk through deploying a static website to an S3 bucket, along with a Lambda
function and API Gateway endpoint to process the submitted form data.

