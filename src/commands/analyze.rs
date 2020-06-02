extern crate vader_sentiment;
use serenity::prelude::*;
use serenity::model::prelude::*;
use serenity::framework::standard::{
    Args, CommandResult,
    macros::command,
};

#[command]
pub fn analyze(ctx: &mut Context, msg: &Message, mut args: Args) -> CommandResult {
    let message = args.single_quoted::<String>().unwrap();
    let (pos, neg, neu) = get_sentiment(&message);

    let _ = msg.channel_id.send_message(&ctx.http, |m| {
        m.embed(|e| {
            e.colour(compute_color(pos, neg, neu));
            e.title("Sentiment Analysis");
            e.description(message);
            e.fields(vec![
                ("Positivity Confidence", format!("{:.2}%",&(pos*100.0)), true),
                ("Negativity Confidence", format!("{:.2}%",&(neg*100.0)), true),
            ]);
            e.field("Neutral Confidence", format!("{:.2}%",&(neu*100.0)), false);
            e.footer(|f| {
                f.text("Sentiment analysis provided by VADER sentiment");

                f
            });

            e
        });
        m
    });

    Ok(())
}

fn compute_color(pos: f64, neg: f64, neu: f64) -> (u8, u8, u8){
    ((255.0*(neg)) as u8, (255.0*(pos)) as u8, (255.0*(neu)) as u8)
}


fn get_sentiment(message: &String) -> (f64, f64, f64){
    let analyzer = vader_sentiment::SentimentIntensityAnalyzer::new();
    let scores = analyzer.polarity_scores(message);

    (*scores.get("pos").unwrap(), *scores.get("neg").unwrap(), *scores.get("neu").unwrap())
}
