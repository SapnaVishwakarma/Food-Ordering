import React, { useState } from 'react';

const Search = () => {
  const [query, setQuery] = useState('');

  const handleSearch = (e) => {
    setQuery(e.target.value);
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-6">
      <div className="max-w-2xl w-full bg-white p-6 rounded-2xl shadow-lg">
        <h1 className="text-3xl font-bold text-gray-800 mb-4 text-center">Search Your Favorite Food</h1>
        <div className="relative flex items-center">
          <input
            type="text"
            placeholder="Search for dishes or restaurants..."
            className="w-full p-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            value={query}
            onChange={handleSearch}
          />
        </div>
        <p className="text-gray-500 mt-4 text-center">Start typing to find delicious meals!</p>
      </div>
    </div>
  );
};

export default Search;
