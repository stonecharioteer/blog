trait CanWave {
    fn get_name(&self) -> &str;
    fn wave(&self) -> String;
}

struct Adult {
    name: String,
}

impl CanWave for Adult {
    fn get_name(&self) -> &str {
        &self.name
    }
    fn wave(&self) -> String {
        String::from("Hey look, I'm an adult waving!")
    }
}

struct Child {
    name: String
}

impl CanWave for Child {
    fn get_name(&self) -> &str {
        &self.name
    }
    fn wave(&self) -> String {
        String::from("gaga, googoo. *waves hands*")
    }
}

struct TrainedDog {
    name: String

}

impl CanWave for TrainedDog {
    fn get_name(&self) -> &str {
        &self.name
    }
    fn wave(&self) -> String {
        String::from("Woof! *waves paw*")
    }
}

struct Dog {
    name: String
}

fn wave_for_me(x: &impl CanWave) {
    println!("{} waves: `{}`", x.get_name(), x.wave());
}

pub fn run() {
    let kumar = Adult { name: "Kumar".to_string()};
    let junior = Child {name: "Junior".to_string()};
    let tiny = TrainedDog {name: "Tiny".to_string()};
    let chotu = Dog {name: "Chotu".to_string()};
    wave_for_me(&kumar);
    wave_for_me(&junior);
    wave_for_me(&tiny);
    // ERROR IF UNCOMMENTED
    // wave_for_me(&chotu);
    // This will not compile because `Dog` doesn't implement CanWave, and thus cannot
    // be used with `wave_for_me`.
    println!("{} hasn't been trained to wave. Maybe you could teach him?", chotu.name);
}
