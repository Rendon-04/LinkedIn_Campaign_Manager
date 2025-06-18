import React, { createContext, useContext, useState, useEffect } from 'react';

const UserContext = createContext();

export const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // For MVP: Hardcoded mock user
    const mockUser = {
      name: 'Ivan Rendon',
      job_goal: 'Software Engineer',
      industry: 'Tech',
      skills: ['React', 'FastAPI', 'PostgreSQL']
    };
    setUser(mockUser);

    //For later use when a user is logged in
    // axios.get("http://localhost:8000/user").then(res => {
    //   setUser(res.data);
    // });
  }, []);

  return (
    <UserContext.Provider value={{ user }}>{children}</UserContext.Provider>
  );
};

export const useUser = () => {
  const context = useContext(UserContext);
  if (!context) {
    throw new Error('useUser must be used within a UserProvider');
  }
  return context;
};
