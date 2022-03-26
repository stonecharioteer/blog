// rustlings structs3.rs
// Structs contain data, but can also have logic. In this exercise we have
// defined the Package struct and we want to test some logic attached to it.
// Make the code compile and the tests pass!
// If you have issues execute `rustlings hint structs3`


#[derive(Debug)]
pub struct Package {
    sender_country: String,
    recipient_country: String,
    weight_in_grams: i32,
}

impl Package {
    pub fn new(sender_country: String, recipient_country: String, weight_in_grams: i32) -> Package {
        if weight_in_grams <= 0 {
            // Something goes here...
            panic!("uh-oh! what do you mean that the weight is negative?");
        } else {
            return Package {
                sender_country,
                recipient_country,
                weight_in_grams,
            };
        }
    }

    pub fn is_international(&self) -> bool {
        self.sender_country != self.recipient_country
    }

    pub fn get_fees(&self, cents_per_gram: i32) -> i32 {
        self.weight_in_grams * cents_per_gram
    }
}
