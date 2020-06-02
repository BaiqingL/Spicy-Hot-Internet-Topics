use serenity::{
    model::{channel::Message, gateway::Ready},
    prelude::*,
};

struct Handler;

impl EventHandler for Handler {

    fn message(&self, ctx: Context, msg: Message) {
        if &msg.content[0..5] == "!rate" {
            if let Err(reason) = msg.channel_id.say(&ctx.http, returnSentiment()) {
                println!("Error sending message: {:?}", reason);
            }
        }
    }

    fn ready(&self, _: Context, ready: Ready) {
        println!("{} is connected!", ready.user.name);
    }
}

fn returnSentiment() -> String {
    String::from("It works")
}

fn main() {

    let token = "token";

    // Create a new instance of the Client, logging in as a bot. This will
    // automatically prepend your bot token with "Bot ", which is a requirement
    // by Discord for bot users.
    let mut client = Client::new(&token, Handler).expect("Err creating client");

    // Finally, start a single shard, and start listening to events.
    //
    // Shards will automatically attempt to reconnect, and will perform
    // exponential backoff until it reconnects.
    if let Err(reason) = client.start() {
        println!("Client error: {:?}", reason);
    }
}