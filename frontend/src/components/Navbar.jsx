import React from 'react'
import '../styles/Navbar.scss'
import {
  FaMagnifyingGlass,
  FaHouseChimney,
  FaUserGroup,
  FaBriefcase,
  FaCommentDots,
  FaBell,
  FaRobot,
  FaCaretDown
} from 'react-icons/fa6'

const Navbar = () => {
  return (
    <header>
      <div className="global-nav__container">
        {/* Logo + Search */}
        <div className="global-nav__searcher">
          <a href="/" className="with-tooltip" data-tooltip="Go to home">
            <figure>
              <img
                src="/images/linkedin-icon.png"
                alt="linkedin logo"
                className="global-nav__logo"
              />
            </figure>
          </a>
          <div className="searcher-container">
            <FaMagnifyingGlass className="fa-magnifying-glass" />
            <input
              type="text"
              className="global-nav__search-bar"
              placeholder="Search"
            />
          </div>
        </div>

        {/* Nav Items */}
        <nav>
          <ul>
            <li>
              <a href="#" className="global-nav__item with-tooltip" data-tooltip="Home">
                <FaHouseChimney />
                <span>Home</span>
              </a>
            </li>
            <li>
              <a href="#" className="global-nav__item with-tooltip" data-tooltip="My Network">
                <FaUserGroup />
                <span>My Network</span>
              </a>
            </li>
            <li>
              <a href="#" className="global-nav__item with-tooltip" data-tooltip="Jobs">
                <FaBriefcase />
                <span>Jobs</span>
              </a>
            </li>
            <li>
              <a href="#" className="global-nav__item with-tooltip" data-tooltip="Messaging">
                <FaCommentDots />
                <span>Messaging</span>
              </a>
            </li>
            <li>
              <a href="#" className="global-nav__item with-tooltip" data-tooltip="Notifications">
                <FaBell />
                <span>Notifications</span>
              </a>
            </li>

            {/* ✅ Campaign Section */}
            <li className='active'>
              <a href="#" className="global-nav__item with-tooltip" data-tooltip="Campaigns">
              <FaRobot />
                <span>Agent</span>
              </a>
            </li>

            {/* ✅ Profile Section */}
            <li className="global-nav__me">
            <a href="#" className="with-tooltip" data-tooltip="Me">
                <div className="profile-img-wrapper">
                <img
                    src="/images/profile.png"
                    alt="Profile"
                    className="profile-img"
                />
                </div>
                <div className="profile-label-wrapper">
                <div className="profile-label">
                    <span>Me</span>
                    <FaCaretDown className="dropdown-arrow" />
                </div>
                </div>
            </a>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  )
}

export default Navbar
