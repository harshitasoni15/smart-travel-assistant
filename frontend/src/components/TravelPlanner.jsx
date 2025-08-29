import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { Badge } from '@/components/ui/badge'
import { Calendar } from '@/components/ui/calendar'
import { Form, FormControl, FormDescription, FormField, FormItem, FormLabel, FormMessage } from '@/components/ui/form'
import { useState } from 'react'
import axios from 'axios'

export function TravelPlanner() {
  const [destination, setDestination] = useState('')
  const [travelers, setTravelers] = useState(1)
  const [dates, setDates] = useState({
    from: new Date(),
    to: new Date()
  })
  const [itinerary, setItinerary] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    
    try {
      const response = await axios.post('http://localhost:3000/api/plan-trip', {
        destination,
        travelers,
        dates: [dates.from.toISOString(), dates.to.toISOString()]
      })
      
      setItinerary(response.data)
    } catch (error) {
      console.error('Error fetching itinerary:', error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6">Smart Travel Assistant</h1>
      
      <Card>
        <CardHeader>
          <CardTitle>Plan Your Trip</CardTitle>
          <CardDescription>Enter your travel details below</CardDescription>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="space-y-2">
              <label htmlFor="destination">Destination</label>
              <Input
                id="destination"
                value={destination}
                onChange={(e) => setDestination(e.target.value)}
                placeholder="e.g., Goa, Delhi"
              />
            </div>
            
            <div className="space-y-2">
              <label htmlFor="travelers">Number of Travelers</label>
              <Select
                onValueChange={(value) => setTravelers(parseInt(value))}
                defaultValue={travelers.toString()}
              >
                <SelectTrigger>
                  <SelectValue placeholder="Select travelers" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="1">1</SelectItem>
                  <SelectItem value="2">2</SelectItem>
                  <SelectItem value="3">3</SelectItem>
                  <SelectItem value="4">4</SelectItem>
                </SelectContent>
              </Select>
            </div>
            
            <div className="space-y-2">
              <label>Date Range</label>
              <Calendar
                mode="range"
                selected={dates}
                onSelect={setDates}
                numberOfMonths={2}
              />
            </div>
            
            <Button type="submit" disabled={loading} className="w-full">
              {loading ? 'Planning...' : 'Plan My Trip'}
            </Button>
          </form>
        </CardContent>
      </Card>
      
      {itinerary && (
        <Card className="mt-6">
          <CardHeader>
            <CardTitle>Travel Itinerary</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div>
                <h3 className="font-semibold">Packing List:</h3>
                <ul className="list-disc pl-5">
                  {itinerary.packing_list.map((item, index) => (
                    <li key={index}>{item}</li>
                  ))}
                </ul>
              </div>
              
              <div>
                <h3 className="font-semibold">Weather Forecast:</h3>
                <p>{itinerary.weather_forecast}</p>
              </div>
              
              <div>
                <h3 className="font-semibold">Booking Links:</h3>
                <div className="space-y-2">
                  {itinerary.booking_links.flights && (
                    <a href={itinerary.booking_links.flights} target="_blank" rel="noopener noreferrer">
                      <Badge variant="outline">Flights</Badge>
                    </a>
                  )}
                  {itinerary.booking_links.hotels && (
                    <a href={itinerary.booking_links.hotels} target="_blank" rel="noopener noreferrer">
                      <Badge variant="outline">Hotels</Badge>
                    </a>
                  )}
                </div>
              </div>
              
              <div>
                <h3 className="font-semibold">Daily Itinerary:</h3>
                {itinerary.itinerary.map((day, index) => (
                  <div key={index} className="mb-4">
                    <h4 className="font-medium">Day {day.day}</h4>
                    <ul className="list-disc pl-5">
                      {day.activities.map((activity, activityIndex) => (
                        <li key={activityIndex}>{activity}</li>
                      ))}
                    </ul>
                  </div>
                ))}
              </div>
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  )
}