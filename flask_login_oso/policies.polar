allow(user: User, "can", "logout");
allow(user: User, "can", "logout") if user.id = "admin";
