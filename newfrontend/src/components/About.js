import React from 'react';

const About = () => {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-6">
      <div className="max-w-4xl bg-white p-8 rounded-2xl shadow-lg text-center">
        <h1 className="text-4xl font-bold text-gray-800 mb-4">About Us</h1>
        <p className="text-gray-600 text-lg mb-6">
          Welcome to <span className="text-blue-600 font-semibold">FoodieExpress</span>, your one-stop destination for delicious meals delivered straight to your doorstep. We bring you a curated selection of the best restaurants, ensuring quality, freshness, and convenience with every order.
        </p>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-4">
          <div className="bg-blue-100 p-6 rounded-xl shadow-sm">
            <h2 className="text-2xl font-semibold text-blue-700">Our Mission</h2>
            <p className="text-gray-600 mt-2">To revolutionize the food delivery experience by offering a seamless and efficient ordering system.</p>
          </div>
          <div className="bg-green-100 p-6 rounded-xl shadow-sm">
            <h2 className="text-2xl font-semibold text-green-700">Why Choose Us?</h2>
            <p className="text-gray-600 mt-2">Fast delivery, diverse cuisine options, and a user-friendly platform designed to satisfy your cravings effortlessly.</p>
          </div>
        </div>
        <p className="text-gray-500 mt-6">Join us and make your mealtime effortless and delightful!</p>
      </div>
    </div>
  );
};

export default About;
